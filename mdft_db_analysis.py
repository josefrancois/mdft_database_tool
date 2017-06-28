import pandas as pd
import os
import mdft_analysis.mdftPlotter as mP
import json
import argparse
import sys


# Put database option to know from which database plots should be generated
arg_parser = argparse.ArgumentParser(prog="mdft_db_analysis.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--database", "-db", help = "Database from which plots will be generated (indicated key in database_definition.json)", default = None)
mdft_args = arg_parser.parse_args()

if mdft_args.database == None:
    sys.exit("Please indicate an input database !")
  
    
# Retrieving of all the necessary informations for the plotting from database_definition.json
with open("database_definition.json", 'r') as json_file:
    db_def = json.load(json_file)
    db_values = db_def[mdft_args.database]['values_to_parse']
    mdft_json = db_def[mdft_args.database]["mdft_output"]
    mdft_db = pd.read_json(mdft_json, orient='index')
    plots = db_def[mdft_args.database]['plots']  
    unit = plots['unit']
    

print mdft_db.shape[0], "solutes" # Printing the number of solutes

# Managing the labels for each involved value
values_label = {}
for value in db_values:
    values_label[value] = db_values[value]['label']    
with open("references/parameters/mdftParsedValues.json", 'r') as json_values:
    mdft_values = json.load(json_values)
    for value in mdft_values:
        values_label[value] = mdft_values[value]['label']


# Creation of a directory to store the various plots
plots_dir = mdft_json[:-5]+"_plots"
os.mkdir(plots_dir)


# Constitution of the plots via mdftPlotter.py
plotter = mP.MdftPlotter(mdft_db, plots_dir)

if "plotsvs" in plots:
    plots_vs = plots['plotsvs'] 
    for plot in plots_vs:
        for value in plots_vs[plot]['y']:
            plotter.plotVS(plots_vs[plot]['x'], value, values_label[plots_vs[plot]['x']], values_label[value], unit)
            
if "plotserrdistrib" in plots :
    plots_errdistrib = plots['plotserrdistrib']     
    for plot in plots_errdistrib:
        values_list = plots_errdistrib[plot]['y']
        plotter.plotErrorDistribution(plotter.calcDiffs(plots_errdistrib[plot]['x'], values_list, values_label[plots_errdistrib[plot]['x']], values_label), plots_errdistrib[plot]['filename'])

if "plotsby" in plots:
    plots_by = plots['plotsby']
    for plot in plots_by:       
        values_list = plots_by[plot]['y']
        plotter.plotErrorby(plotter.calcErrorby(plots_by[plot]['x'], values_list, values_label, plots_by[plot]['cat_column']), plots_by[plot]['cat_column']) 

# Copying the output JSON file from the parsing step into the plots directory    
os.system("cp " + mdft_json + " ./"+plots_dir)
