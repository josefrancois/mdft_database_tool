import sys

if len(sys.argv) != 4:
    sys.exit("NOTICE : python mdft_db_process.py boxlen boxnod mmax")
    
import os
import mdft_parser.parserGro as pG
import mdft_parser.parserTop as pT
import mdft_parser.parserJson as pJ

from mdft_writer.writers import *

topgro_list = "topgro/"
input_mdft = "input_mdft/"



os.mkdir('input_mdft')
input_files = os.listdir(topgro_list)

json_file = ""
for f in os.listdir('.'):
    if f[-5:] == ".json":
        json_file = f


for input_file in input_files:    
    atom_listcoord = pG.ParserGro()
    atom_list = pT.ParserTop()
    energy = pJ.ParserJson()
    input_name = input_file[:-4]
    energy.nameSyst(input_name)
    if os.path.exists(input_mdft+input_name):
        continue
    else:
        os.mkdir(input_mdft+input_name)
        print input_name
    energy.getInfos(json_file)  
    atom_listcoord.getCoord(os.path.join(topgro_list, input_name + ".gro"))
    atom_list.getAtoms(os.path.join(topgro_list, input_name + ".top"))
    writeSoluteIn(input_mdft+input_name, energy.syst, energy.exp_dg, energy.calc_dg, \
                  atom_list.list_num, atom_list.list_charge, atom_list.list_sigma, atom_list.list_epsilon, atom_list.list_atomname, \
                  atom_listcoord.list_x, atom_listcoord.list_y, atom_listcoord.list_z, \
                  atom_list.list_mass)
    writeDftIn(input_mdft+input_name, sys.argv[1], sys.argv[2], sys.argv[3], 298.15)
    writeDoFile(input_mdft+input_name)
    
#os.system("tar -czvf ./input_mdft.tar.gz ./input_mdft/")
