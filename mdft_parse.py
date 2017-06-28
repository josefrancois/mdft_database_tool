import os
import mdft_parser.parserJson as pJ
import mdft_parser.parserLog as pL
import mdft_writer.jsonWriter as jW
import argparse
import glob
import json


# Put a database option to merge MDFT results with the values of the submitted database if needed
arg_parser = argparse.ArgumentParser(prog="mdft_parse.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--database","-db", help = "Database to parse (indicated key in database_definition.json)", default = None)
mdft_args = arg_parser.parse_args()


# Parse database_definition.json to retrieve the name of the database of reference values and the name of the output JSON file
with open('database_definition.json', 'r') as json_file:
    db_def = json.load(json_file)
    
    
# Creation of two parsers : one for the database, the second for the output from MDFT calculations
pJson = pJ.ParserJson()
pLog = pL.ParserLog()


# Constitution of the list of the folders containing the MDFT results to be parsed 
solute_dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d) and d not in ['mdft-dev','references','mdft_parser', 'mdft_writer']]


# Parsing of the reference and MDFT values which will be retrieved in the dictionary mdft_database 
mdft_database = {}

for solute_dir in solute_dirs:
    print solute_dir
    log_file = max(glob.iglob(solute_dir+'/'+'*.out'), key=os.path.getsize) # Parsing the most large output file which is most likely to contain the MDFT results 
    mdft_values = pLog.parse(log_file)
    if len(mdft_values) != 0: # Parsing only if MDFT has converged
    	if mdft_args.database != None and "ref_values" in db_def[mdft_args.database]: # If reference values are provided, MDFT values are merged with them  	    
            input_name = db_def[mdft_args.database]
            ref_values = input_name["ref_values"] 
    	    pJson.parseData(ref_values, solute_dir) # Parsing of reference values...
    	    mdft_database[solute_dir] = pJson.getData() # ...and putting them into mdft_database dictionary
    	    for mdft_value in mdft_values:
	    	mdft_database[solute_dir][mdft_value] = mdft_values[mdft_value] # Adding of MDFT values mdft_database dictionary
    	else: # If no reference values are provided, the output JSON file will contain only MDFT values
		mdft_database[solute_dir] = mdft_values  
    else: # Avoid solutes for which no MDFT results are retrieved
	    continue


# From the mdft_database dictionary, writing of the output JSON file containing either reference+MDFT values or only MDFT values
newJson = jW.JsonWriter(mdft_database)
if mdft_args.database != None and "ref_values" in db_def[mdft_args.database]:
    newJson.write(db_def[mdft_args.database]['mdft_output'])
else:
    newJson.write('mdft.json')
