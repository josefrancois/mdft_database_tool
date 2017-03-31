#import sys

#if len(sys.argv) != 4:
#    sys.exit("NOTICE : python mdft_db_process.py boxlen boxnod mmax")
import os
import mdft_parser.gromacsParser as gP
import mdft_parser.parserJson as pJ
import mdft_writer.mdftWriter as mW
import argparse


#os.system("git clone https://github.com/maxlevesque/mdft-dev")


arg_parser = argparse.ArgumentParser(prog="mdft_db_process.py")

arg_parser.add_argument("--json", help = "JSON file to parse")
arg_parser.add_argument("--topgro", help = "Folder which contains top and gro files to parse")
arg_parser.add_argument("--boxlen", "-l", help = "Length of box size", type=float)
arg_parser.add_argument("--boxnod", "-n", help = "Number of nodes", type=int)
arg_parser.add_argument("--solvent", help = "Solvent to use in MDFT")
arg_parser.add_argument("--mmax", help = "Maximum number of orientations of solvent molecules to consider")
arg_parser.add_argument("--temperature","-T", help = "Temperature to use in MDFT", type=float)
mdft_args = arg_parser.parse_args()


if mdft_args.topgro is not None:
    topgro_files = mdft_args.topgro+"/"
else:
    topgro_files = "minitopgro/"
input_mdft = "input_mdft/"

if os.path.exists(input_mdft) == False:
    os.mkdir('input_mdft')
    
input_files = os.listdir(topgro_files)

if mdft_args.json is not None:
    json_file = mdft_args.json
else:
    for actual_file in os.listdir('.'):
        if actual_file[-5:] == ".json":
            json_file = actual_file
#print json_file

param_mdft = {'L':mdft_args.boxlen, 'N':mdft_args.boxnod, 'solvent':mdft_args.solvent, 'mmax':mdft_args.mmax, 'temperature':mdft_args.temperature}

for input_file in input_files:    
    input_name = input_file[:-4]
    
    if os.path.exists(input_mdft+input_name):
        #print input_name
        pass
    else:
        os.mkdir(input_mdft+input_name)
        os.system("ln -s "+ os.getcwd() + "/mdft-dev/build/data " + input_mdft+input_name +"/data")
        os.system("ln -s " + os.getcwd() + "mdft-dev/build/mdft-dev " + input_mdft+input_name +"/mdft-dev")
        print input_name       
        parser = gP.GromacsParser(topgro_files+input_name + ".gro", topgro_files+input_name + ".top")
        molecule = parser.parse()
                                                    
        fjson = pJ.ParserJson()
        fjson.parseData(json_file, input_name)
        molecule.setData(fjson.getDataSolute() )
        molecule.setName(fjson.getSoluteName() )
        #print molecule.getData
                                                                              
        writer = mW.MdftWriter(molecule, param_mdft)
        writer.write(input_mdft+input_name)
        os.chdir(input_mdft+input_name)
        os.system("./mdft-dev | tee " + input_name +".log")
        os.chdir("../..")
        
        
    




#os.system("tar -czvf ./input_mdft.tar.gz ./input_mdft/")
