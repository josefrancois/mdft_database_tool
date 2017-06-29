import argparse
from mdft_parser.parserSolutein import *
import mdft_writer.jsonWriter as jW
import json

# Set solutein and databases options to know which solute.in file to parse and to which JSON database the data should be added
arg_parser = argparse.ArgumentParser(prog="solutein_to_json.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--solutein", help = "solute.in file to parse", default = None)
arg_parser.add_argument("--database", "-db", help = "Database where the molecule will be added", default = "mdft_database.json")
mdft_args = arg_parser.parse_args()

solute = SoluteinParser()

molecule = Molecule()

with open(mdft_args.database, 'r') as json_file:
    mdft_db = json.load(json_file)
    
    if mdft_args.solutein is not None :
        solute.parse(mdft_args.solutein)   
        #print molecule
        mdft_db[solute.getName()] = {}
        print solute.getName()
        for i in range(solute.getNumberOfAtoms()):         
            mdft_db[solute.getName()]['atom'+str((i+1))] = {} # Creating one dictionary for each atom of the solute
            atom = mdft_db[solute.getName()]['atom'+str((i+1))]
            atom['name'] = 'atom'+str((i+1))
            atom['index'] = solute.getListNum()[i]
            atom['x'] = solute.getListx()[i]
            atom['y'] = solute.getListy()[i]
            atom['z'] = solute.getListz()[i]
            atom['charge'] = solute.getListCharge()[i]
            atom['epsilon'] = solute.getListEpsilon()[i]
            atom['sigma'] = solute.getListSigma()[i]
            atom['Zatomic'] = int(solute.getListNumatom()[i])
            print mdft_db
            
        newJson = jW.JsonWriter(mdft_db)
        newJson.write(mdft_args.database)
    else:
        pass

# Bash script to execute it on several solute.in files stored in a folder:
# for folder in *; do if [ -d $folder -a $folder == "**Name of the folder**" ]; then for molecule in $folder/*; do python solutein_to_json.py -db  **Name of the JSON database**.json --solutein $molecule; done fi done
