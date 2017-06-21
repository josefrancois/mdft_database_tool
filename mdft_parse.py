import os
import mdft_parser.parserJson as pJ
import mdft_parser.parserLog as pL
import mdft_writer.jsonWriter as jW
import argparse
import glob

arg_parser = argparse.ArgumentParser(prog="mdft_parse.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--database","-db", help = "Database to parse", default = None)
mdft_args = arg_parser.parse_args()

pJson = pJ.ParserJson()
pLog = pL.ParserLog()

solute_dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d) and d not in ['mdft-dev','references','mdft_parser', 'mdft_writer']]


mdft_database = {}

for solute_dir in solute_dirs:
    print solute_dir
    log_file = max(glob.iglob(solute_dir+'/'+'*.out'), key=os.path.getsize)#Parsing the most large output file which is most likely to contain the MDFT results 
    mdft_values = pLog.parse(log_file)
    #print len(mdft_values),
    if len(mdft_values) != 0: #Avoid solutes for which no MDFT results are retrieved
    	if mdft_args.database != None: #If reference values of SFE are provided, MDFT values are merged with them 
    		pJson.parseData(mdft_args.database, solute_dir)
    		mdft_database[solute_dir] = pJson.getData()
    		for mdft_value in mdft_values:
			mdft_database[solute_dir][mdft_value] = mdft_values[mdft_value]
    	else:
	   	    mdft_database[solute_dir] = mdft_values #If no ref values are provided, the output JSON 
    else:
	    continue

newJson = jW.JsonWriter(mdft_database)
newJson.write('mdft.json')






























