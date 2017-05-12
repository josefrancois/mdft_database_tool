"""
Project : MDFT Database Tool

Author : Jose Francois
"""

import os
import mdft_parser.gromacsParser as gP
import mdft_parser.mdftdbParser as mdP
import mdft_parser.parserJson as pJ
import mdft_writer.mdftWriter as mW
import mdft_writer.runAllWriter as rAW
import json
import argparse

arg_parser = argparse.ArgumentParser(prog="mdft_db_process.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

arg_parser.add_argument("--json", help = "JSON file to parse", default = "mobley.json")
arg_parser.add_argument("--mdftdatabase", "-mdftdb", help = "MDFT DataBase to parse", default = None)
arg_parser.add_argument("--topgro", help = "Folder which contains top and gro files to parse", default = "minitopgro")
arg_parser.add_argument("--voxelsize", "-dx", help = "Distance between two nodes [unit : angstroms]", type=float, default = 0.5)
arg_parser.add_argument("--lenbulk", "-lb", help = "Distance between solute and box sides [unit : angstroms]", type=int, default = 10)
arg_parser.add_argument("--solvent", help = "Solvent to use in MDFT")
arg_parser.add_argument("--mmax", help = "Maximum number of orientations of solvent molecules to consider", type=int, default = 1)
arg_parser.add_argument("--temperature","-T", help = "Temperature to use in MDFT [unit : Celsius degree]", type=float, default = 298.15)
arg_parser.add_argument("--server", "-sv", help = "Server machine in which MDFT calculations would be performed", default = "abalone")
arg_parser.add_argument("--mdftcommit", help = "Commit hash of mdft-dev that should be used", default = None)
arg_parser.add_argument("--mdftpath", help = "Path of mdft-dev if already compiled", default = None)
arg_parser.add_argument("--bridge", "-bg", help = "Bridge Functional to use in MDFT calculations", default = "none")
arg_parser.add_argument("--solute_charges_scale_factor", "-scsf", help = "Solute charges factor which indicates how much we consider the influence of the partial charges", default = 1)


mdft_args = arg_parser.parse_args()

topgro_files = mdft_args.topgro+"/"
json_file = mdft_args.json


if mdft_args.bridge == 'none' :
    input_mdft = "input_mdft/"
else:
    input_mdft = "input_mdft_"+ mdft_args.bridge +'/'

if os.path.exists(input_mdft) == False:
    os.mkdir(input_mdft)
    
input_files = os.listdir(topgro_files)

#print json_file

param_mdft = {'lb':mdft_args.lenbulk, 'dx':mdft_args.voxelsize, 'solvent':mdft_args.solvent, \
              'mmax':mdft_args.mmax, 'temperature':mdft_args.temperature, 'bridge':mdft_args.bridge, \
              'solute_charges_scale_factor':mdft_args.solute_charges_scale_factor}

run_writer = rAW.runAllWriter() 

if mdft_args.mdftdatabase is None:
    for input_file in input_files:    
        input_name = input_file[:-4]
        
        if os.path.exists(input_mdft+input_name):
            #print input_name
            pass
        else:
            os.mkdir(input_mdft + input_name)
            print input_name       
            parser = gP.GromacsParser(topgro_files+input_name + ".gro", topgro_files+input_name + ".top")
            molecule = parser.parse()
                                                        
            fjson = pJ.ParserJson()
            fjson.parseData(json_file, input_name)
            molecule.setData(fjson.getData() )
            molecule.setName(fjson.getRecordName() )
            #print molecule.getData
                                                                                  
            writer = mW.MdftWriter(molecule, param_mdft)
            writer.write(input_mdft+input_name)
            os.system("cp ./references/do_files/" + run_writer.getDoFile(mdft_args.server)+ " " + input_mdft+input_name)
else:
    with open(mdft_args.mdftdatabase, 'r') as fjson:
        mdft_database = json.load(fjson)
    
    for mol in mdft_database:    
        parser = mdP.MdftDBParser(mdft_database)
        molecule = parser.parse(mol)
        molecule.setName(mol)
        os.mkdir(input_mdft+molecule.getName())
        writer = mW.MdftWriter(molecule, param_mdft)
        writer.write(input_mdft+molecule.getName())
        os.system("cp ./references/do_files/" + run_writer.getDoFile(mdft_args.server)+ " " + input_mdft+molecule.getName())
 
run_writer.write(mdft_args.server, mdft_args.mdftcommit, input_mdft)      

os.system("cp mdft_parse.py " + input_mdft)
os.system("cp -r mdft_parser "  + input_mdft)
os.system("cp -r mdft_writer "  + input_mdft)
os.system("cp -r references " + input_mdft)
os.system("cp " + json_file + " " + input_mdft)

if mdft_args.mdftpath is not None :
    os.system("cp -r " + mdft_args.mdftpath + " " + input_mdft)
os.system("tar -czvf " + input_mdft[:-1] + ".tar.gz " +input_mdft)
