""" Common functions for package biobb_analysis.ambertools """
import os.path
from biobb_common.tools import file_utils as fu


def check_top_path(path):
	""" Checks topology input file """ 
	if not os.path.exists(path):
		raise SystemExit('Unexisting topology input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_topology(file_extension[1:]):
		raise SystemExit('Format %s in topology input file is not compatible' % file_extension[1:])
	return path

def check_traj_path(path):
	""" Checks trajectory input file """ 
	if not os.path.exists(path):
		raise SystemExit('Unexisting trajectory input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_trajectory(file_extension[1:]):
		raise SystemExit('Format %s in trajectory input file is not compatible' % file_extension[1:])
	return path

def check_out_path(path):
	""" Checks if output folder exists """
	if not os.path.exists(os.path.dirname(path)):
		raise SystemExit('Unexisting output folder')
	return path

def check_conf(path):
	""" Checks configuration file """
	if not os.path.exists(path):
		raise SystemExit('Unexisting configuration file')
	return path

def get_parameters(properties, type):
	""" Gets in_parameters and out_parameters """
	if not properties.get(type, dict()):
		raise SystemExit('No ' + type + ' parameters provided')
	else:
		return {k: v for k, v in properties.get(type, dict()).items()}

def get_binary_path(properties, type):
	""" Gets binary path """
	return properties.get(type, get_default_value(type))

def check_in_path(path, obj):
	""" Checks input instructions file """ 
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)
	if not os.path.exists(path):
		fu.log('Unexisting input instructions file, exiting', out_log, obj.global_log)
		raise SystemExit('Unexisting input instructions file')

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
		fu.log('Incorrect syntax for instructions file: %s, exiting' % err_instructions, out_log, obj.global_log)
		raise SystemExit('Incorrect syntax for instructions file: %s, exiting' % err_instructions)

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
		"cpptraj_path": "cpptraj"
	}

	return default_values[key]

def is_valid_topology(ext):
	""" Checks if trajectory format is compatible with Cpptraj """
	formats = 'top', 'pdb', 'prmtop', 'parmtop'
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

def get_in_parameters(list, obj, type = 'None'):
	""" Return string with input parameters """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)

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
				fu.log('No start value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('start'), out_log, obj.global_log)
			if not end: 
				end = str(get_default_value("end"))
				fu.log('No end value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('end'), out_log, obj.global_log)
			if not step: 
				step = str(get_default_value("step"))
				fu.log('No step value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('step'), out_log, obj.global_log)
	else:
		# check if trajin parameters are provided and have correct format
		if(type == 'snapshot'):
			snapshot = str(get_default_value("snapshot")) if not 'snapshot' in list else str(list['snapshot'])
			if not 'snapshot' in list or not list['snapshot'] or not isinstance(list['snapshot'], int):
				snapshot = str(get_default_value("snapshot"))
				fu.log('No snapshot value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('snapshot'), out_log, obj.global_log)
			start = snapshot
			end = snapshot
			step = '1'
		else:
			start = str(get_default_value("start")) if not 'start' in list else str(list['start'])
			if not 'start' in list or not list['start'] or not isinstance(list['start'], int):
				start = str(get_default_value("start"))
				fu.log('No start value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('start'), out_log, obj.global_log)
			end = str(get_default_value("end")) if not 'end' in list else str(list['end'])
			if not 'end' in list or not list['end'] or not isinstance(list['end'], int):
				end = str(get_default_value("end"))
				fu.log('No end value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('end'), out_log, obj.global_log)
			step = str(get_default_value("step")) if not 'step' in list else str(list['step'])
			if not 'step' in list or not list['step'] or not isinstance(list['step'], int):
				step = str(get_default_value("step"))
				fu.log('No step value provided in configuration file or incorrect format, assigned default value: %s' % get_default_value('step'), out_log, obj.global_log)

	# TODO: validate end > start? 

	return start + " " + end + " " + step

def setup_structure(obj):
	""" Sets up the structure """
	instructions_list = []
	mask_atoms = get_mask('heavy-atoms', obj)
	instructions_list.append('center ' + mask_atoms + ' origin')
	instructions_list.append('autoimage')
	instructions_list.append('rms first ' + mask_atoms)
	mask_solvent = get_mask('solvent', obj)
	mask_ions = get_mask('ions', obj)
	instructions_list.append('strip ' + mask_solvent + ',' + mask_ions[1:])

	return instructions_list


def get_negative_mask(key, obj):
	""" Gives the negative mask according to the given key """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)
	atoms, msg = get_mask_atoms(key)
	if atoms[0] == '!':
		mask = atoms[1:]
	else:
		mask = '!' + atoms
	# if mask incorrect, give message
	if msg: 
		fu.log(msg, out_log, obj.global_log)

	return mask

def get_mask(key, obj):
	""" Gives mask according to the given key """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)
	mask, msg = get_mask_atoms(key)
	# if mask incorrect, give message
	if msg: 
		fu.log(msg, out_log, obj.global_log)

	return mask

def get_reference(ref, obj, mask, output):
	""" Gives reference instructions according to the given key """
	instructions_list = []

	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)
	if not ref or ref == 'None':
		ref = get_default_value('reference')
		fu.log('No reference provided in configuration file, assigned default value: %s' % get_default_value('reference'), out_log, obj.global_log)

	if not is_valid_reference(ref):
		fu.log('Reference %s is not compatible, assigned default value: %s' % (ref, get_default_value('reference')), out_log, obj.global_log)
		ref = get_default_value('reference')

	if ref == 'first':
		if output: instructions_list.append('rms first out ' + obj.output_cpptraj_path)
		else: instructions_list.append('rms first')

	if ref == 'average':
		instructions_list.append('average crdset ' + get_default_value('average'))
		instructions_list.append('run')
		if output: instructions_list.append('rms ref ' + get_default_value('average') + ' ' + mask + ' out ' + obj.output_cpptraj_path)
		else: instructions_list.append('rms ref ' + get_default_value('average') + ' ' + mask)

	if ref == 'experimental':
		if not obj.input_exp_path:
			fu.log('No experimental structure provided, exiting', out_log, obj.global_log)
			raise SystemExit('input_exp_path is mandatory')
		instructions_list.append('parm ' + obj.input_exp_path + ' noconect [exp]')
		solute, msg = get_mask_atoms('solute')
		instructions_list.append('reference ' + obj.input_exp_path + ' ' + solute + ' parm [exp]')
		backbone, msg = get_mask_atoms('backbone')
		if output: instructions_list.append('rms reference ' + backbone + ' ' + mask + ' out ' + obj.output_cpptraj_path)
		else: instructions_list.append('rms reference ' + backbone + ' ' + mask)


	return instructions_list

def get_out_parameters(list, obj):
	""" Return string with output parameters """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)

	format = list['format']
	msg = None
	 # check if format provided
	if not format:
		format = get_default_value('format')
		fu.log('No format provided in configuration file, assigned default value: %s' % get_default_value('format'), out_log, obj.global_log)
	# check if valid format
	if not is_valid_trajectory(format):
		fu.log('Format %s is not compatible, assigned default value: %s' % (format, get_default_value('format')), out_log, obj.global_log)
		format = get_default_value('format')

	return format