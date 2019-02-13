""" Common functions for package biobb_analysis.ambertools """
from biobb_common.tools import file_utils as fu
from ast import literal_eval

def get_default_value(key):
	""" Gives default values according to the given key """
	default_values = {
		"start": 1,
		"end": -1,
		"step": 1,
		"snapshot": 1,
		"format": "netcdf",
		"mask": "all-atoms"
	}

	return default_values[key]

def is_valid_format(traj):
	""" Checks if trajectory format is compatible with Cpptraj """
	formats = ['crd', 'cdf', 'netcdf', 'restart', 'ncrestart', 'restartnc', 'dcd', 'charmm', 'cor', 'pdb', 'mol2', 'trr', 'gro', 'binpos', 'xtc', 'cif', 'arc', 'sqm', 'sdf', 'conflib']
	if traj in formats:
		return True
	else:
		return False

def get_mask_atoms(key):
	""" Gives mask atoms according to the given key """
	masks = {
		"c-alpha": "@CA",
		"backbone": "@C,CA,N,O,C3',O3',C4',C5',O5',P",
		"all-atoms": ":*",
		"heavy-atoms": "!@H*,1H*,2H*,3H*",
		"side-chain": "!@CA,C,N,O,H,HA,C3',O3',C4',C5',O5',P",
		"solute": "!:WAT,SOL,TIP3,TP3",
		"ions": ":SOD,CLA,Na+,Cl-,NA,CL,K+,K",
		"solvent": ":WAT,SOL,TIP3,TP3"
	}

	# if key incorrect, return default value and message 
	if key in masks:
		return masks[key], None
	else:
		return masks[get_default_value("mask")], "Mask %s is not compatible, assigned default value: %s" % (key, get_default_value("mask"))

def get_in_parameters(list, obj, type = 'None'):
	""" Return string with input parameters """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)
	list = literal_eval(list)

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

def get_out_parameters(list, obj):
	""" Return string with output parameters """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)
	list = literal_eval(list)
	format = list['format']
	msg = None
	 # check if format provided
	if not format:
		format = get_default_value('format')
		fu.log('No format provided in configuration file, assigned default value: %s' % get_default_value('format'), out_log, obj.global_log)
	# check if valid format
	if not is_valid_format(format):
		fu.log('Format %s is not compatible, assigned default value: %s' % (format, get_default_value('format')), out_log, obj.global_log)
		format = get_default_value('format')

	return format