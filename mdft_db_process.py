#import sys

#if len(sys.argv) != 4:
#    sys.exit("NOTICE : python mdft_db_process.py boxlen boxnod mmax")
import os
import mdft_parser.gromacsParser as gP
import mdft_writer.mdftWriter as mW

topgro_list = "minitopgro/"
input_mdft = "input_mdft/"

#if os.path.exists(input_mdft) == False:
os.mkdir('input_mdft')
	
input_files = os.listdir(topgro_list)

json_file = ""
for actual_file in os.listdir('.'):
    if actual_file[-5:] == ".json":
        json_file = actual_file


for input_file in input_files:    
    input_name = input_file[:-4]
    
    if os.path.exists(input_mdft+input_name):
        continue
    else:
        os.mkdir(input_mdft+input_name)
        print input_name
        
    molecule = gP.parse(topgro_list+input_name + ".gro", topgro_list+input_name + ".top", json_file)
    
    mW.writeMdftFiles(input_mdft+input_name, molecule)


#writeDoFile(input_mdft+input_name)    
#os.system("tar -czvf ./input_mdft.tar.gz ./input_mdft/")
