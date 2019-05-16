""" Common functions for package biobb_analysis.gromacs """
import os.path
from os import listdir
from biobb_common.tools import file_utils as fu


def check_energy_path(path, out_log, classname):
	""" Checks energy input file """ 
	if not os.path.exists(path):
		fu.log(classname + ': Unexisting energy input file, exiting', out_log)
		raise SystemExit(classname + ': Unexisting energy input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_energy(file_extension[1:]):
		fu.log(classname + ': Format %s in energy input file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in energy input file is not compatible' % file_extension[1:])
	return path

def check_input_path(path, out_log, classname):
	""" Checks input structure file """ 
	if not os.path.exists(path):
		fu.log(classname + ': Unexisting structure input file, exiting', out_log)
		raise SystemExit(classname + ': Unexisting structure input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_structure(file_extension[1:]):
		fu.log(classname + ': Format %s in structure input file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in structure input file is not compatible' % file_extension[1:])
	return path

def check_traj_path(path, out_log, classname):
	""" Checks input structure file """ 
	if not os.path.exists(path):
		fu.log(classname + ': Unexisting trajectory input file, exiting', out_log)
		raise SystemExit(classname + ': Unexisting trajectory input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_trajectory(file_extension[1:]):
		fu.log(classname + ': Format %s in trajectory input file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in trajectory input file is not compatible' % file_extension[1:])
	return path

def check_out_xvg_path(path, out_log, classname):
	""" Checks if output folder exists and format is xvg """
	if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
		fu.log(classname + ': Unexisting output folder, exiting', out_log)
		raise SystemExit(classname + ': Unexisting output folder')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_xvg(file_extension[1:]):
		fu.log(classname + ': Format %s in output file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in output file is not compatible' % file_extension[1:])
	return path

def check_out_pdb_path(path, out_log, classname):
	""" Checks if output folder exists and format is xvg """
	if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
		fu.log(classname + ': Unexisting output folder, exiting', out_log)
		raise SystemExit(classname + ': Unexisting output folder')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_structure(file_extension[1:]):
		fu.log(classname + ': Format %s in output file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in output file is not compatible' % file_extension[1:])
	return path

def check_out_traj_path(path, out_log, classname):
	""" Checks if output folder exists and format is correct """
	if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
		fu.log(classname + ': Unexisting output folder, exiting', out_log)
		raise SystemExit(classname + ': Unexisting output folder')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_trajectory_output(file_extension[1:]):
		fu.log(classname + ': Format %s in output file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in output file is not compatible' % file_extension[1:])
	return path

def check_out_str_ens_path(path, out_log, classname):
	""" Checks if output folder exists and format is correct """
	if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
		fu.log(classname + ': Unexisting output folder, exiting', out_log)
		raise SystemExit(classname + ': Unexisting output folder')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_zip(file_extension[1:]):
		fu.log(classname + ': Format %s in output file is not compatible' % file_extension[1:], out_log)
		raise SystemExit(classname + ': Format %s in output file is not compatible' % file_extension[1:])
	return path

def get_default_value(key):
	""" Gives default values according to the given key """
	default_values = {
		"instructions_file": "instructions.in",
		"gmx_path": "gmx",
		"terms": ["Potential"],
		"selection": "System",
		"xvg": "none",
		"dista": False,
		"method": "linkage",
		"cutoff": 0.1,
		"center_selection": "Protein-H",
	  	"output_selection": "Protein-H",
	  	"pbc": "mol",
	  	"center": True,
	  	"fit": "none",
	  	"ur": "compact",
	  	"start": 0,
	  	"end": 0,
	  	"dt": 0,
	  	"ot_str_ens": "pdb"
	}

	return default_values[key]

def get_binary_path(properties, type):
	""" Gets binary path """
	return properties.get(type, get_default_value(type))

def get_terms(properties, out_log, classname):
	""" Gets energy terms """
	terms = properties.get('terms', dict())
	if not terms or not isinstance(terms, list):
		fu.log(classname + ': No terms provided or incorrect format, exiting', out_log)
		raise SystemExit(classname + ': No terms provided or incorrect format')
	if not is_valid_term(terms):
		fu.log(classname + ': Incorrect terms provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect terms provided')
	return properties.get('terms', '')

def get_selection(properties, out_log, classname):
	""" Gets selection items """
	selection = properties.get('selection', get_default_value('selection'))
	if not selection:
		fu.log(classname + ': No selection provided or incorrect format, exiting', out_log)
		raise SystemExit(classname + ': No selection provided or incorrect format')
	if not is_valid_selection(selection):
		fu.log(classname + ': Incorrect selection provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect selection provided')
	return selection

def get_image_selection(properties, key, out_log, classname):
	""" Gets selection items """
	selection = properties.get(key, get_default_value(key))
	if not selection:
		fu.log(classname + ': No selection provided or incorrect format, exiting', out_log)
		raise SystemExit(classname + ': No selection provided or incorrect format')
	if not is_valid_selection(selection):
		fu.log(classname + ': Incorrect selection provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect selection provided')
	return selection

def get_pbc(properties, out_log, classname):
	""" Gets pbc """
	pbc = properties.get('pbc', get_default_value('pbc'))
	if not is_valid_pbc(pbc):
		fu.log(classname + ': Incorrect pbc provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect pbc provided')
	return pbc

def get_center(properties, out_log, classname):
	""" Gets center """
	center = properties.get('center', get_default_value('center'))
	if not is_valid_boolean(center):
		fu.log(classname + ': Incorrect center provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect center provided')
	return center

def get_ur(properties, out_log, classname):
	""" Gets ur """
	ur = properties.get('ur', get_default_value('ur'))
	if not is_valid_ur(ur):
		fu.log(classname + ': Incorrect ur provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect ur provided')
	return ur

def get_fit(properties, out_log, classname):
	""" Gets fit """
	fit = properties.get('fit', get_default_value('fit'))
	if not is_valid_fit(fit):
		fu.log(classname + ': Incorrect fit provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect fit provided')
	return fit

def get_start(properties, out_log, classname):
	""" Gets start """
	start = properties.get('start', get_default_value('start'))
	if not is_valid_int(start):
		fu.log(classname + ': Incorrect start provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect start provided')
	return str(start)

def get_end(properties, out_log, classname):
	""" Gets end """
	end = properties.get('end', get_default_value('end'))
	if not is_valid_int(end):
		fu.log(classname + ': Incorrect end provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect end provided')
	return str(end)

def get_dt(properties, out_log, classname):
	""" Gets dt """
	dt = properties.get('dt', get_default_value('dt'))
	if not is_valid_int(dt):
		fu.log(classname + ': Incorrect dt provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect dt provided')
	return str(dt)

def get_ot_str_ens(properties, out_log, classname):
	""" Gets output type """
	output_type = properties.get('output_type', get_default_value('ot_str_ens'))
	if not is_valid_ot_str_ens(output_type):
		fu.log(classname + ': Incorrect output_type provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect output_type provided')
	return str(output_type)

def get_xvg(properties, out_log, classname):
	""" Gets xvg """
	xvg = properties.get('xvg', get_default_value('xvg'))
	if not is_valid_xvg_param(xvg):
		fu.log(classname + ': Incorrect xvg provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect xvg provided')
	return xvg

def get_dista(properties, out_log, classname):
	""" Gets dista """
	dista = properties.get('dista', get_default_value('dista'))
	if not is_valid_boolean(dista):
		fu.log(classname + ': Incorrect dista provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect dista provided')
	return dista

def get_method(properties, out_log, classname):
	""" Gets method """
	method = properties.get('method', get_default_value('method'))
	if not is_valid_method_param(method):
		fu.log(classname + ': Incorrect method provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect method provided')
	return method

def get_cutoff(properties, out_log, classname):
	""" Gets cutoff """
	cutoff = properties.get('cutoff', get_default_value('cutoff'))
	if not is_valid_float(cutoff):
		fu.log(classname + ': Incorrect cutoff provided, exiting', out_log)
		raise SystemExit(classname + ': Incorrect cutoff provided')
	return str(cutoff)

def is_valid_boolean(val):
	""" Checks if given value is boolean """
	values = [True, False]
	return val in values

def is_valid_float(val):
	""" Checks if given value is float """
	if val and not isinstance(val, float) and not isinstance(val, int):
		return False
	return True

def is_valid_int(val):
	""" Checks if given value is int """
	if val and not isinstance(val, int):
		return False
	return True

def is_valid_method_param(met):
	""" Checks if method is compatible with GROMACS """
	methods = ['linkage', 'jarvis-patrick', 'monte-carlo', 'diagonalization', 'gromos']
	return met in methods

def is_valid_structure(ext):
	""" Checks if structure format is compatible with GROMACS """
	formats = ['tpr', 'gro', 'g96', 'pdb', 'brk', 'ent']
	return ext in formats

def is_valid_trajectory(ext):
	""" Checks if trajectory format is compatible with GROMACS """
	formats = ['xtc', 'trr', 'cpt', 'gro', 'g96', 'pdb', 'tng']
	return ext in formats

def is_valid_trajectory_output(ext):
	""" Checks if trajectory format is compatible with GROMACS """
	formats = ['xtc', 'trr', 'gro', 'g96', 'pdb', 'tng']
	return ext in formats

def is_valid_energy(ext):
	""" Checks if energy format is compatible with GROMACS """
	formats = ['edr']
	return ext in formats

def is_valid_xvg(ext):
	""" Checks if file is XVG """
	formats = ['xvg']
	return ext in formats

def is_valid_zip(ext):
	""" Checks if file is ZIP """
	formats = ['zip']
	return ext in formats

def is_valid_xvg_param(ext):
	""" Checks xvg parameter """
	formats = ['xmgrace', 'xmgr', 'none']
	return ext in formats

def is_valid_ot_str_ens(ext):
	""" Checks if output type for structure ensemble is correct """
	formats = ['gro', 'g96', 'pdb']
	return ext in formats

def is_valid_pbc(pbc):
	""" Checks pbc parameter """
	values = ['none', 'mol', 'res', 'atom', 'nojump', 'cluster', 'whole']
	return pbc in values

def is_valid_ur(ur):
	""" Checks ur parameter """
	values = ['rect', 'tric', 'compact']
	return ur in values

def is_valid_fit(fit):
	""" Checks fit parameter """
	values = ['none', 'rot+trans', 'rotxy+transxy', 'translation', 'transxy', 'progressive']
	return fit in values

def is_valid_term(iterms):
	""" Checks if term is correct """
	cterms = ['Angle', 'Proper-Dih.', 'Improper-Dih.', 'LJ-14', 'Coulomb-14', 'LJ-(SR)', 'Coulomb-(SR)', 'Coul.-recip.', 'Position-Rest.', 'Potential', 'Kinetic-En.', 'Total-Energy', 'Temperature', 'Pressure', ' Constr.-rmsd', 'Box-X', 'Box-Y', ' Box-Z', 'Volume', 'Density', 'pV', 'Enthalpy', 'Vir-XX', 'Vir-XY', 'Vir-XZ', 'Vir-YX', 'Vir-YY', 'Vir-YZ', 'Vir-ZX', 'Vir-ZY', 'Vir-ZZ', 'Pres-XX', 'Pres-XY', 'Pres-XZ', 'Pres-YX', 'Pres-YY', 'Pres-YZ', 'Pres-ZX', 'Pres-ZY', 'Pres-ZZ', '#Surf*SurfTen', 'Box-Vel-XX', 'Box-Vel-YY', 'Box-Vel-ZZ', 'Mu-X', 'Mu-Y', 'Mu-Z', 'T-Protein', 'T-non-Protein', 'Lamb-Protein', 'Lamb-non-Protein']
	return all(elem in cterms for elem in iterms)

def is_valid_selection(ext):
	""" Checks if selection is correct """
	formats = ['System', 'Protein', 'Protein-H', 'C-alpha', 'Backbone', 'MainChain', 'MainChain+Cb', 'MainChain+H', 'SideChain', 'SideChain-H', 'Prot-Masses', 'non-Protein', 'Water', 'SOL', 'non-Water', 'Ion', 'NA', 'CL', 'Water_and_ions']
	return ext in formats

def remove_tmp_files(list, out_log):
	""" Removes temporal files generated by the wrapper """
	tmp_files = list
	removed_files = [f for f in tmp_files if fu.rm(f)]
	fu.log('Removed: %s' % str(removed_files), out_log)

def process_output_trjconv_str_ens(tmp_folder, output_file, out_log):
	""" Compresses, moves and removes temporal files generated by the wrapper """
	# list all files in temporary folder
	tmp_fl = os.listdir( tmp_folder )
	files_list = []
	for file_name in tmp_fl:
		files_list.append(os.path.join(tmp_folder, file_name))

	# adding files from temporary folder to zip
	fu.zip_list(output_file, files_list, out_log)

	# remove temporary folder
	fu.rm(tmp_folder)
	fu.log('Removed temporary folder: %s' % tmp_folder, out_log)
