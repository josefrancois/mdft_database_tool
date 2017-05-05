import os
import mdft_parser.parserJson as pJ
import mdft_parser.parserLog as pL
import mdft_writer.jsonWriter as jW

json_file = "mobley.json"

pJson = pJ.ParserJson()
pLog = pL.ParserLog()

solute_dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

mdft_database = {}

for solute_dir in solute_dirs:
	for mdft_file in os.listdir(solute_dir):
		if mdft_file[-4:] == ".out":
            pJson.parseData(json_file, solute_dir)
            mdft_database = pJson.getData()
	                print solute_dir
			log_file = mdft_file
			pJson.parseData(json_file, solute_dir)
			mdft_database[solute_dir] = pLog.parse(solute_dir+'/'+log_file)
			

newJson = jW.JsonWriter(mdft_database)
newJson.write('mdft.json')






























