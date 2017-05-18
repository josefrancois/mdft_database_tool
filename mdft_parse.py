import os
import mdft_parser.parserJson as pJ
import mdft_parser.parserLog as pL
import mdft_writer.jsonWriter as jW
import argparse

arg_parser = argparse.ArgumentParser(prog="mdft_parse.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--database","-db", help = "Database to parse", default = None)
mdft_args = arg_parser.parse_args()

pJson = pJ.ParserJson()
pLog = pL.ParserLog()

solute_dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

mdft_database = {}

for solute_dir in solute_dirs:
	for mdft_file in os.listdir(solute_dir):
		if mdft_file[-4:] == ".out":
		    log_file = mdft_file
		    mdft_values = pLog.parse(solute_dir+'/'+log_file)
		    if mdft_args.database != None:
		    	pJson.parseData(mdft_args.database, solute_dir)
		    	mdft_database[solute_dir] = pJson.getData()
		    	for mdft_value in mdft_values:
				    mdft_database[solute_dir][mdft_value] = mdft_values[mdft_value]
		    else:
			    mdft_database[solute_dir] = mdft_values
		    print solute_dir

newJson = jW.JsonWriter(mdft_database)
newJson.write('mdft.json')






























