""" Common functions for package biobb_analysis.ambertools """
from pathlib import Path, PurePath
import zipfile
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu


def unzip_top_path(path, tmp_files, out_log):
    """ Returns the topology extracted from path if it is a zip file, path otherwise.
    The folder of the extracted topology is added to the tmp_files list """
    if not zipfile.is_zipfile(path):
        return path
    top_file = fu.unzip_top(zip_file=path, out_log=out_log)
    tmp_files.append(str(PurePath(top_file).parent))
    return top_file


def check_in_path(path, out_log, classname):
    """ Checks input instructions file """
    if not Path(path).exists():
        fu.log(classname + ': Unexisting input instructions file, exiting', out_log)
        raise SystemExit(classname + ': Unexisting input instructions file')

    # check syntax for instructions file
    syntax_instructions = True
    err_instructions = ''
    if 'parm ' not in open(path).read():
        syntax_instructions = False
        err_instructions += 'No topology provided'
    if 'trajin ' not in open(path).read():
        syntax_instructions = False
        err_instructions += ' No input trajectory provided'
    if not syntax_instructions:
        fu.log(classname + ': Incorrect syntax for instructions file: %s, exiting' % err_instructions, out_log)
        raise SystemExit(classname + ': Incorrect syntax for instructions file: %s, exiting' % err_instructions)


def get_default_value(key):
    """ Gives default values according to the given key """
    default_values = {
        "start": 1,
        "end": -1,
        "step": 1,
        "snapshot": 1,
        "format": "netcdf",
        "mask": "all-atoms",
        "reference": "first",
        "average": "MyAvg",
        "instructions_file": "instructions.in",
        "algorithm": "hieragglo",
        "metric": "rms",
        "linkage": "linkage",
        "cluster_set": "MyClusters",
    }

    return default_values[key]


def is_valid_trajectory(traj):
    """ Checks if trajectory format is compatible with Cpptraj """
    formats = 'mdcrd', 'crd', 'cdf', 'netcdf', 'nc', 'restart', 'ncrestart', 'restartnc', 'dcd', 'charmm', 'cor', 'pdb', 'mol2', 'trr', 'gro', 'binpos', 'xtc', 'cif', 'arc', 'sqm', 'sdf', 'conflib'
    return traj in formats


def is_valid_reference(ref):
    """ Checks if reference is correct """
    references = 'first', 'average', 'experimental'
    return ref in references


def is_valid_cluster_algorithm(algorithm):
    """ Checks if clustering algorithm is compatible with Cpptraj """
    algorithms = 'hieragglo', 'dbscan', 'kmeans', 'dpeaks'
    return algorithm in algorithms


def is_valid_cluster_metric(metric):
    """ Checks if clustering distance metric is compatible with Cpptraj """
    metrics = 'rms', 'srmsd', 'dme', 'qrmsd'
    return metric in metrics


def is_valid_cluster_linkage(linkage):
    """ Checks if hierarchical agglomerative linkage is compatible with Cpptraj """
    linkages = 'linkage', 'averagelinkage', 'complete'
    return linkage in linkages


def get_cluster_algorithm(algorithm, clusters, epsilon, minpoints, linkage, out_log):
    """ Return string with the clustering algorithm keywords """
    if not algorithm or algorithm == 'None':
        algorithm = get_default_value('algorithm')
        fu.log('No algorithm provided in configuration file, assigned default value: %s' % get_default_value('algorithm'), out_log)

    if not is_valid_cluster_algorithm(algorithm):
        fu.log('Algorithm %s is not compatible, assigned default value: %s' % (algorithm, get_default_value('algorithm')), out_log)
        algorithm = get_default_value('algorithm')

    if algorithm == 'hieragglo':
        if not is_valid_cluster_linkage(linkage):
            fu.log('Linkage %s is not compatible, assigned default value: %s' % (linkage, get_default_value('linkage')), out_log)
            linkage = get_default_value('linkage')
        keywords = ['hieragglo', 'clusters', str(clusters), linkage]
        # epsilon is an additional stop condition for hieragglo, only added when provided
        if epsilon is not None and epsilon > 0:
            keywords += ['epsilon', str(epsilon)]
    elif algorithm == 'kmeans':
        keywords = ['kmeans', 'clusters', str(clusters)]
    else:
        # both dbscan and dpeaks need epsilon
        if epsilon is None or epsilon <= 0:
            fu.log('Algorithm %s needs a positive epsilon, assigned default value: 1.0' % algorithm, out_log)
            epsilon = 1.0
        if algorithm == 'dbscan':
            keywords = ['dbscan', 'minpoints', str(minpoints), 'epsilon', str(epsilon)]
        else:
            keywords = ['dpeaks', 'epsilon', str(epsilon), 'choosepoints', 'auto']

    return ' '.join(keywords)


def get_cluster_metric(metric, mass, nofit, metric_mask, out_log):
    """ Return string with the clustering distance metric keywords """
    if not metric or metric == 'None':
        metric = get_default_value('metric')
        fu.log('No metric provided in configuration file, assigned default value: %s' % get_default_value('metric'), out_log)

    if not is_valid_cluster_metric(metric):
        fu.log('Metric %s is not compatible, assigned default value: %s' % (metric, get_default_value('metric')), out_log)
        metric = get_default_value('metric')

    keywords = [metric]
    if mass:
        keywords.append('mass')
    if nofit:
        keywords.append('nofit')

    if not metric_mask or metric_mask == 'None':
        metric_mask = get_default_value('mask')
        fu.log('No metric_mask provided in configuration file, assigned default value: %s' % get_default_value('mask'), out_log)
    # the metric mask selects atoms, it does not remove them from the clustered coordinates
    keywords.append(get_mask(metric_mask))

    return ' '.join(keywords)


def get_traj_format(path, out_log):
    """ Return the Cpptraj trajectory format matching the extension of the given path """
    format = PurePath(path).suffix[1:]
    if not is_valid_trajectory(format):
        fu.log('Format %s is not compatible, assigned default value: %s' % (format, get_default_value('format')), out_log)
        format = get_default_value('format')

    return format


def get_in_parameters(list, out_log, type='None'):
    """ Return string with input parameters """
    # if strip or mask, no mandatory trajin parameters
    if type == 'strip' or type == 'mask':
        start = '' if 'start' not in list else str(list['start'])
        end = '' if 'end' not in list else str(list['end'])
        step = '' if 'step' not in list else str(list['step'])
        if (not start or start == 'None') and (not end or end == 'None') and (not step or step == 'None'):
            return ''
        else:
            if not start:
                start = str(get_default_value("start"))
                fu.log('No start value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('start'), out_log)
            if not end:
                end = str(get_default_value("end"))
                fu.log('No end value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('end'), out_log)
            if not step:
                step = str(get_default_value("step"))
                fu.log('No step value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('step'), out_log)
    else:
        # check if trajin parameters are provided and have correct format
        if (type == 'snapshot'):
            snapshot = str(get_default_value("snapshot")) if 'snapshot' not in list else str(list['snapshot'])
            if 'snapshot' not in list or not list['snapshot'] or not isinstance(list['snapshot'], int):
                snapshot = str(get_default_value("snapshot"))
                fu.log('No snapshot value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('snapshot'), out_log)
            start = snapshot
            end = snapshot
            step = '1'
        else:
            start = str(get_default_value("start")) if 'start' not in list else str(list['start'])
            if 'start' not in list or not list['start'] or not isinstance(list['start'], int):
                start = str(get_default_value("start"))
                fu.log('No start value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('start'), out_log)
            end = str(get_default_value("end")) if 'end' not in list else str(list['end'])
            if 'end' not in list or not list['end'] or not isinstance(list['end'], int):
                end = str(get_default_value("end"))
                fu.log('No end value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('end'), out_log)
            step = str(get_default_value("step")) if 'step' not in list else str(list['step'])
            if 'step' not in list or not list['step'] or not isinstance(list['step'], int):
                step = str(get_default_value("step"))
                fu.log('No step value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('step'), out_log)

            # checking start <= end
            if end != '-1' and int(start) > int(end):
                fu.log('End must be -1 (indicating the end of the trajectory) or more or equal than start. Your values are start: %s, end: %s' % (start, end), out_log)
                raise SystemExit('End must be -1 (indicating the end of the trajectory) or greater or equal than start. Your values are start: %s, end: %s' % (start, end))

    return start + " " + end + " " + step


def setup_structure():
    """ Sets up the structure """
    instructions_list = []
    mask_atoms = get_mask('heavy-atoms')
    instructions_list.append('center ' + mask_atoms + ' origin')
    instructions_list.append('autoimage')
    instructions_list.append('rms first ' + mask_atoms)
    instructions_list.append('strip ' + get_mask('solvent') + ',' + get_mask('ions')[1:])

    return instructions_list


MASKS = {
    "c-alpha": "@CA",
    "backbone": "@C,CA,N,O,C3',O3',C4',C5',O5',P",
    "all-atoms": ":*",
    "heavy-atoms": "!@H*,1H*,2H*,3H*",
    "side-chain": "!@CA,C,N,O,H,HA,C3',O3',C4',C5',O5',P",
    "solute": "!:WAT,HOH,SOL,TIP3,TP3,SOD,CLA,Na+,Cl-,NA,CL,K+,K",
    "ions": ":SOD,CLA,Na+,Cl-,NA,CL,K+,K",
    "solvent": ":WAT,HOH,SOL,TIP3,TP3"
}


def get_mask(key):
    """ Goes from a mask name (or an Amber mask) to the Amber mask """
    return MASKS.get(key, key)


def get_negative_mask(key):
    """ Goes from a mask name (or an Amber mask) to the Amber mask of the other atoms """
    mask = get_mask(key)
    return mask[1:] if mask[0] == '!' else '!' + mask


def get_reference(ref, output_cpptraj_path, input_exp_path, mask, output, classname, out_log, nofit=False, norotate=False, nomod=False):
    """ Gives reference instructions according to the given key """
    instructions_list = []
    if not ref or ref == 'None':
        ref = get_default_value('reference')
        fu.log('No reference provided in configuration file, assigned default value: %s' % get_default_value('reference'), out_log)

    if not is_valid_reference(ref):
        fu.log('Reference %s is not compatible, assigned default value: %s' % (ref, get_default_value('reference')), out_log)
        ref = get_default_value('reference')

    # end of the rms line: output file and flags
    rms_end = ' out ' + output_cpptraj_path if output else ''
    rms_end += ''.join(' ' + flag for flag, value in (('nofit', nofit), ('norotate', norotate), ('nomod', nomod)) if value)

    if ref == 'first':
        instructions_list.append('rms first' + rms_end)

    if ref == 'average':
        instructions_list.append('average crdset ' + get_default_value('average'))
        instructions_list.append('run')
        instructions_list.append('rms ref ' + get_default_value('average') + ' ' + mask + rms_end)

    if ref == 'experimental':
        if not input_exp_path:
            fu.log('No experimental structure provided, exiting', out_log)
            raise SystemExit(classname + ': input_exp_path is mandatory')
        instructions_list.append('parm ' + input_exp_path + ' noconect [exp]')
        instructions_list.append('reference ' + input_exp_path + ' ' + get_mask('solute') + ' parm [exp]')
        instructions_list.append('rms reference ' + mask + rms_end)

    return instructions_list


def get_out_parameters(format, out_log):
    """ Return string with output parameters """
    # check if format provided
    if not format:
        format = get_default_value('format')
        fu.log('No format provided in configuration file, assigned default value: %s' % get_default_value('format'), out_log)
    # check if valid format
    if not is_valid_trajectory(format):
        fu.log('Format %s is not compatible, assigned default value: %s' % (format, get_default_value('format')), out_log)
        format = get_default_value('format')

    return format


class CpptrajBase(BiobbObject):
    """Parent of the cpptraj blocks: goes from the instructions of the block to a cpptraj run
    on input_top_path and input_traj_path."""

    def prepare(self) -> None:
        """Extract the topology from input_top_path if it is a zip file."""
        self.io_dict["in"]["input_top_path"] = unzip_top_path(self.io_dict["in"]["input_top_path"], self.tmp_files, self.out_log)

    def trajin_frames(self) -> str:
        """Goes from the start, end and steps properties to the frames of the trajin line."""
        return get_in_parameters({'start': self.start, 'end': self.end, 'step': self.steps}, self.out_log)

    def instructions(self) -> list[str]:
        """Goes from the properties to the cpptraj instructions that follow the parm and trajin lines."""
        raise NotImplementedError

    def strip_mask(self) -> list[str]:
        """Goes from the mask property to the strip line that keeps only its atoms (none without mask)."""
        return ['strip ' + get_negative_mask(self.mask)] if self.mask else []

    def trajout(self) -> str:
        """Goes from output_cpptraj_path and the format property to the trajout line."""
        return 'trajout ' + self.stage_io_dict["out"]["output_cpptraj_path"] + ' ' + get_out_parameters(self.format, self.out_log)

    def run(self) -> None:
        """Write the instructions file in the sandbox and run cpptraj with it."""
        instructions = ['parm ' + self.stage_io_dict["in"]["input_top_path"],
                        'trajin ' + self.stage_io_dict["in"]["input_traj_path"] + ' ' + self.trajin_frames()]
        instructions += self.instructions()
        instructions_file = self.create_tmp_file(get_default_value('instructions_file'))
        with open(instructions_file, 'w') as file:
            file.writelines(line.strip() + '\n' for line in instructions)
        self.cmd = [self.binary_path, '-i', self.staged_path(instructions_file)]
        self.run_biobb()
