import sys

if len(sys.argv) != 4:
    sys.exit("NOTICE : python mdft_db_process.py boxlen boxnod mmax")
    
import os
import mdft_parser.gromacsParser
import mdft_writer.mdftWriter

topgro_list = "minitopgro/"
input_mdft = "input_mdft/"

os.mkdir('input_mdft')
input_files = os.listdir(topgro_list)

json_file = ""
for actual_file in os.listdir('.'):
    if f[-5:] == ".json":
        json_file = actual_file


for input_file in input_files:    
    input_name = input_file[:-4]
    energy.nameSyst(input_name)
    if os.path.exists(input_mdft+input_name):
        continue
    else:
        os.mkdir(input_mdft+input_name)
        print input_name
    
    writeMdftFiles(
    writeDoFile(input_mdft+input_name)
    
#os.system("tar -czvf ./input_mdft.tar.gz ./input_mdft/")
