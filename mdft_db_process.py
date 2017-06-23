"""
Project : MDFT Database Tool

Author : Jose Francois
"""

import os
import mdft_parser.gromacsParser as gP
import mdft_parser.jsondbParser as jdP
import mdft_writer.mdftWriter as mW
import mdft_writer.runAllWriter as rAW
import dbCloner as dbC
import json
import argparse


arg_parser = argparse.ArgumentParser(prog="mdft_db_process.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--database", "-db", help = "Database to parse", default = None)
arg_parser.add_argument("--voxelsize", "-dx", help = "Distance between two nodes [unit : angstroms]", type=float, default = 0.5)
arg_parser.add_argument("--lenbulk", "-lb", help = "Distance between solute and box sides [unit : angstroms]", type=int, default = 10)
arg_parser.add_argument("--solvent", help = "Solvent to use in MDFT")
arg_parser.add_argument("--mmax", help = "Maximum number of orientations of solvent molecules to consider", type=int, default = 1)
arg_parser.add_argument("--temperature","-T", help = "Temperature to use in MDFT [unit : Kelvin]", type=float, default = 298.15)
arg_parser.add_argument("--server", "-sv", help = "Server machine in which MDFT calculations would be performed", default = "abalone")
arg_parser.add_argument("--mdftcommit", help = "Commit hash of mdft-dev that should be used", default = None)
arg_parser.add_argument("--mdftpath", help = "Path of mdft-dev if already compiled", default = None)
arg_parser.add_argument("--bridge", "-bg", help = "Bridge Functional to use in MDFT calculations", default = "none")
arg_parser.add_argument("--solute_charges_scale_factor", "-scsf", help = "Solute charges factor which indicates how much we consider the influence of the partial charges", default = 1)
arg_parser.add_argument("--direct_solute_sigmak", "-dss", help = "Guillaume Jeanmairet's implementation", default = 'F')
mdft_args = arg_parser.parse_args()


if mdft_args.bridge == 'none' :
    input_mdft = mdft_args.database+'/'
else:
    input_mdft = mdft_args.database+ "_"+ mdft_args.bridge +'/'

if os.path.exists(input_mdft) == False:
    os.mkdir(input_mdft)
    

param_mdft = {'lb':mdft_args.lenbulk, 'dx':mdft_args.voxelsize, 'solvent':mdft_args.solvent, \
              'mmax':mdft_args.mmax, 'temperature':mdft_args.temperature, 'bridge':mdft_args.bridge, \
              'solute_charges_scale_factor':mdft_args.solute_charges_scale_factor,\
              'direct_solute_sigmak': mdft_args.direct_solute_sigmak}
              

with open('database_definition.json', 'r') as json_file:
    db_def = json.load(json_file)
input_name = db_def[mdft_args.database]
db_format = input_name["format"] 
parser = None
input_db_name = None
if db_format == 'gromacs':
    if "github" in input_name:
        cloner = dbC.DBCloner(input_name["github"], input_name["mol_db"])
        input_db_name = cloner.write()
        cloner.execute()
    else:
        input_db_name = input_name["mol_db"]   
    parser = gP.GromacsParser(input_db_name)    
    input_db = list(set([f[:-4] for f in os.listdir(input_db_name) if ".gro" in f]))
elif db_format == 'json':
    with open(input_name["mol_db"], 'r') as fjson:
        input_db = json.load(fjson)
    parser = jdP.JsonDBParser(input_db)
    
    
run_writer = rAW.runAllWriter()

for mol in input_db:
    print mol
    molecule = parser.parse(mol)
    molecule.setName(mol)
    os.mkdir(input_mdft+molecule.getName())
    writer = mW.MdftWriter(molecule, param_mdft)
    writer.write(input_mdft+molecule.getName())
    os.system("cp ./references/do_files/" + run_writer.getDoFile(mdft_args.server)+ " " + input_mdft+molecule.getName())

run_writer.write(mdft_args.server, mdft_args.mdftcommit, input_mdft)    
  

os.system("cp mdft_parse.py " + input_mdft)
os.system("cp database_definition.json " + input_mdft)
os.system("cp -r mdft_parser "  + input_mdft)
os.system("cp -r mdft_writer "  + input_mdft)
os.system("cp -r references " + input_mdft)

if mdft_args.mdftpath is not None :
    os.system("cp -r " + mdft_args.mdftpath + " " + input_mdft)
os.system("tar -czvf " + input_mdft[:-1] + ".tar.gz " +input_mdft)
