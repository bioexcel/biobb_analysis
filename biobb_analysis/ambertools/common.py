""" Common functions for package biobb_analysis.ambertools """
import os.path
import zipfile
from biobb_common.tools import file_utils as fu


def check_top_path(path, out_log, classname):
	""" Checks topology input file """ 
	orig_path = path
	if not os.path.exists(path):
		fu.log(classname + ': Unexisting topology input file, exiting', out_log)
		raise SystemExit(classname + ': Unexisting topology input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_topology(file_extension[1:]):
		fu.log(classname + ': Format %s in topology input file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in topology input file is not compatible' % file_extension[1:])
	if zipfile.is_zipfile(path):
		top_file = fu.unzip_top(zip_file=path, out_log=out_log)
		path = top_file
	return path, orig_path

def check_traj_path(path, out_log, classname):
	""" Checks trajectory input file """ 
	if not os.path.exists(path):
		fu.log(classname + ': Unexisting trajectory input file, exiting', out_log)
		raise SystemExit(classname + ': Unexisting trajectory input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_trajectory(file_extension[1:]):
		fu.log(classname + ': Format %s in trajectory input file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in trajectory input file is not compatible' % file_extension[1:])
	return path

def check_out_path(path, out_log, classname):
	""" Checks if output folder exists """
	if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
		fu.log(classname + ': Unexisting output folder, exiting', out_log)
		raise SystemExit(classname + ': Unexisting output folder')
	return path

def get_parameters(properties, type, classname, out_log):
	""" Gets in_parameters and out_parameters """
	if not properties.get(type, dict()):
		fu.log('No %s parameters provided' % type, out_log)
		return get_default_value(classname)[type]

	return {k: v for k, v in properties.get(type, dict()).items()}

def get_binary_path(properties, type):
	""" Gets binary path """
	return properties.get(type, get_default_value(type))

def check_in_path(path, out_log, classname):
	""" Checks input instructions file """ 
	if not os.path.exists(path):
		fu.log(classname + ': Unexisting input instructions file, exiting', out_log)
		raise SystemExit(classname + ': Unexisting input instructions file')

	# check syntax for instructions file
	syntax_instructions = True
	err_instructions = ''
	if not 'parm ' in open(path).read():
		syntax_instructions = False
		err_instructions += 'No topology provided'
	if not 'trajin ' in open(path).read():
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
		"cpptraj_path": "cpptraj",
		# default conf for Average
		"Average": {
			"in_parameters": {
				"start": 1,
				"end": -1,
				"step": 1,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "pdb"
			}
		},
		# default conf for Bfactor
		"Bfactor": {
			"in_parameters": {
			    "start": 1,
			    "end": -1,
			    "step": 1,
			    "mask": "all-atoms",
			    "reference": "first"
			}
		},
		# default conf for Convert
		"Convert": {
			"in_parameters": {
				"start": 1,
				"end": -1,
				"step": 1,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "netcdf"
			}
		},
		# default conf for Dry
		"Dry": {
			"in_parameters": {
				"start": 1,
				"end": -1,
				"step": 1,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "netcdf"
			}
		},
		# default conf for Image
		"Image": {
			"in_parameters": {
				"start": 1,
				"end": -1,
				"step": 1,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "netcdf"
			}
		},
		# default conf for Mask
		"Mask": {
			"in_parameters": {
				"start": 1,
				"end": -1,
				"step": 1,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "netcdf"
			}
		},
		# default conf for Rgyr
		"Rgyr": {
			"in_parameters": {
			    "start": 1,
			    "end": -1,
			    "step": 1,
			    "mask": "all-atoms"
			}
		},
		# default conf for Rms
		"Rms": {
			"in_parameters": {
			    "start": 1,
			    "end": -1,
			    "step": 1,
			    "mask": "all-atoms",
			    "reference": "first"
			}
		},
		# default conf for Rmsf
		"Rmsf": {
			"in_parameters": {
			    "start": 1,
			    "end": -1,
			    "step": 1,
			    "mask": "all-atoms",
			    "reference": "first"
			}
		},
		# default conf for Slice
		"Slice": {
			"in_parameters": {
				"start": 1,
				"end": -1,
				"step": 1,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "netcdf"
			}
		},
		# default conf for Snapshot
		"Snapshot": {
			"in_parameters": {
				"snapshot": 12,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "pdb"
			}
		},
		# default conf for Strip
		"Strip": {
			"in_parameters": {
				"start": 1,
				"end": -1,
				"step": 1,
				"mask": "all-atoms"
			},
			"out_parameters": {
				"format": "netcdf"
			}
		}
	}

	return default_values[key]

def is_valid_topology(ext):
	""" Checks if trajectory format is compatible with Cpptraj """
	formats = 'top', 'pdb', 'prmtop', 'parmtop', 'zip'
	return ext in formats

def is_valid_trajectory(traj):
	""" Checks if trajectory format is compatible with Cpptraj """
	formats = 'crd', 'cdf', 'netcdf', 'restart', 'ncrestart', 'restartnc', 'dcd', 'charmm', 'cor', 'pdb', 'mol2', 'trr', 'gro', 'binpos', 'xtc', 'cif', 'arc', 'sqm', 'sdf', 'conflib'
	return traj in formats

def is_valid_reference(ref):
	""" Checks if reference is correct """
	references = 'first', 'average', 'experimental'
	return ref in references

def get_mask_atoms(key):
	""" Gives mask atoms according to the given key """
	masks = {
		"c-alpha": "@CA",
		"backbone": "@C,CA,N,O,C3',O3',C4',C5',O5',P",
		"all-atoms": ":*",
		"heavy-atoms": "!@H*,1H*,2H*,3H*",
		"side-chain": "!@CA,C,N,O,H,HA,C3',O3',C4',C5',O5',P",
		"solute": "!:WAT,HOH,SOL,TIP3,TP3",
		"ions": ":SOD,CLA,Na+,Cl-,NA,CL,K+,K",
		"solvent": ":WAT,HOH,SOL,TIP3,TP3"
	}

	# if key incorrect, return default value and message 
	if key in masks:
		return masks[key], None
	else:
		return masks[get_default_value("mask")], "Mask %s is not compatible, assigned default value: %s" % (key, get_default_value("mask"))

def get_in_parameters(list, out_log, type = 'None'):
	""" Return string with input parameters """
	# if strip or mask, no mandatory trajin parameters
	if type == 'strip' or type == 'mask':
		start = '' if not 'start' in list else str(list['start'])
		end = '' if not 'end' in list else str(list['end'])
		step = '' if not 'step' in list else str(list['step'])
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
		if(type == 'snapshot'):
			snapshot = str(get_default_value("snapshot")) if not 'snapshot' in list else str(list['snapshot'])
			if not 'snapshot' in list or not list['snapshot'] or not isinstance(list['snapshot'], int):
				snapshot = str(get_default_value("snapshot"))
				fu.log('No snapshot value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('snapshot'), out_log)
			start = snapshot
			end = snapshot
			step = '1'
		else:
			start = str(get_default_value("start")) if not 'start' in list else str(list['start'])
			if not 'start' in list or not list['start'] or not isinstance(list['start'], int):
				start = str(get_default_value("start"))
				fu.log('No start value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('start'), out_log)
			end = str(get_default_value("end")) if not 'end' in list else str(list['end'])
			if not 'end' in list or not list['end'] or not isinstance(list['end'], int):
				end = str(get_default_value("end"))
				fu.log('No end value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('end'), out_log)
			step = str(get_default_value("step")) if not 'step' in list else str(list['step'])
			if not 'step' in list or not list['step'] or not isinstance(list['step'], int):
				step = str(get_default_value("step"))
				fu.log('No step value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('step'), out_log)

			# checking start <= end
			if end != '-1' and start > end:
				fu.log('End must be -1 (indicating the end of the trajectory) or more or equal than start. Your values are start: %s, end: %s' % (start, end), out_log)
				raise SystemExit('End must be -1 (indicating the end of the trajectory) or greater or equal than start. Your values are start: %s, end: %s' % (start, end))

	return start + " " + end + " " + step

def setup_structure(out_log):
	""" Sets up the structure """
	instructions_list = []
	mask_atoms = get_mask('heavy-atoms', out_log)
	instructions_list.append('center ' + mask_atoms + ' origin')
	instructions_list.append('autoimage')
	instructions_list.append('rms first ' + mask_atoms)
	mask_solvent = get_mask('solvent', out_log)
	mask_ions = get_mask('ions', out_log)
	instructions_list.append('strip ' + mask_solvent + ',' + mask_ions[1:])

	return instructions_list

def get_negative_mask(key, out_log):
	""" Gives the negative mask according to the given key """
	atoms, msg = get_mask_atoms(key)
	if atoms[0] == '!':
		mask = atoms[1:]
	else:
		mask = '!' + atoms
	# if mask incorrect, give message
	if msg: 
		fu.log(msg, out_log)

	return mask

def get_mask(key, out_log):
	""" Gives mask according to the given key """
	mask, msg = get_mask_atoms(key)
	# if mask incorrect, give message
	if msg: 
		fu.log(msg, out_log)

	return mask

def get_reference(ref, output_cpptraj_path, input_exp_path, mask, output, classname):
	""" Gives reference instructions according to the given key """
	instructions_list = []
	if not ref or ref == 'None':
		ref = get_default_value('reference')
		fu.log('No reference provided in configuration file, assigned default value: %s' % get_default_value('reference'), out_log)

	if not is_valid_reference(ref):
		fu.log('Reference %s is not compatible, assigned default value: %s' % (ref, get_default_value('reference')), out_log)
		ref = get_default_value('reference')

	if ref == 'first':
		if output: instructions_list.append('rms first out ' + output_cpptraj_path)
		else: instructions_list.append('rms first')

	if ref == 'average':
		instructions_list.append('average crdset ' + get_default_value('average'))
		instructions_list.append('run')
		if output: instructions_list.append('rms ref ' + get_default_value('average') + ' ' + mask + ' out ' + output_cpptraj_path)
		else: instructions_list.append('rms ref ' + get_default_value('average') + ' ' + mask)

	if ref == 'experimental':
		if not input_exp_path:
			fu.log('No experimental structure provided, exiting', out_log)
			raise SystemExit(classname + ': input_exp_path is mandatory')
		instructions_list.append('parm ' + input_exp_path + ' noconect [exp]')
		solute, msg = get_mask_atoms('solute')
		instructions_list.append('reference ' + input_exp_path + ' ' + solute + ' parm [exp]')
		backbone, msg = get_mask_atoms('backbone')
		if output: instructions_list.append('rms reference ' + mask + ' out ' + output_cpptraj_path)
		else: instructions_list.append('rms reference ' + mask)


	return instructions_list

def get_out_parameters(list, out_log):
	""" Return string with output parameters """
	format = list['format']
	msg = None
	 # check if format provided
	if not format:
		format = get_default_value('format')
		fu.log('No format provided in configuration file, assigned default value: %s' % get_default_value('format'), out_log)
	# check if valid format
	if not is_valid_trajectory(format):
		fu.log('Format %s is not compatible, assigned default value: %s' % (format, get_default_value('format')), out_log)
		format = get_default_value('format')

	return format

def remove_tmp_files(list, out_log, input_top_path_orig = None, input_top_path = None):
	""" Removes temporal files generated by the wrapper """
	tmp_files = list
	if zipfile.is_zipfile(input_top_path_orig):
		tmp_files.append(os.path.dirname(input_top_path))
	removed_files = [f for f in tmp_files if fu.rm(f)]
	fu.log('Removed: %s' % str(removed_files), out_log)