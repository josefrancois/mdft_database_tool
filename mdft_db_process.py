#import sys

#if len(sys.argv) != 4:
#    sys.exit("NOTICE : python mdft_db_process.py boxlen boxnod mmax")
import os
import mdft_parser.gromacsParser as gP
import mdft_parser.parserJson as pJ
import mdft_writer.mdftWriter as mW

topgro_list = "topgro/"
input_mdft = "input_mdft/"

if os.path.exists(input_mdft) == False:
	os.mkdir('input_mdft')
    
input_files = os.listdir(topgro_list)

json_file = ""
for actual_file in os.listdir('.'):
    if actual_file[-5:] == ".json":
        json_file = actual_file

#print json_file

for input_file in input_files:    
    input_name = input_file[:-4]
    
    if os.path.exists(input_mdft+input_name):
        print input_name
        pass
    else:
        os.mkdir(input_mdft+input_name)
        print input_name
        
    parser = gP.GromacsParser(topgro_list+input_name + ".gro", topgro_list+input_name + ".top")
    molecule = parser.parse()
    
    fjson = pJ.ParserJson()
    fjson.parseData(json_file, input_name)
    molecule.setData(fjson.getDataSolute() )
    molecule.setName(fjson.getSoluteName() )
    #print molecule.getData
        
    writer = mW.MdftWriter(molecule)
    writer.write(input_mdft+input_name)


#writeDoFile(input_mdft+input_name)    
#os.system("tar -czvf ./input_mdft.tar.gz ./input_mdft/")
