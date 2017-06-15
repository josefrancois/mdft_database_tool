import pandas as pd
import os
import mdft_analysis.mdftPlotter as mP
import json
import argparse

arg_parser = argparse.ArgumentParser(prog="mdft_db_analysis.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#arg_parser.add_argument("--json", help = "JSON file to parse", default = "mdft.json")
arg_parser.add_argument("--mdft_database", "-mdft_db", help = "Database for which MDFT will be compared", default = "mobley")
mdft_args = arg_parser.parse_args()


with open("database_definition.json", 'r') as json_file:
    db_def = json.load(json_file)
    db_values = db_def[mdft_args.mdft_database]['values_to_parse']
    mdft_json = db_def[mdft_args.mdft_database]["mdft_output"]
    mdft_db = pd.read_json(mdft_json, orient='index')
    plots = db_def[mdft_args.mdft_database]['plots']
    plots_vs = plots['plotvs']
    plots_errdistrib = plots['errordistrib']
    plots_by = plots['plotsby']
    unit = plots['unit']
    
#mdft_db = pd.read_json(mdft_args.json, orient='index')

print mdft_db.shape[0], "solutes"


values_label = {}
for value in db_values:
    values_label[value] = db_values[value]['label']    
with open("references/parameters/mdftParsedValues.json", 'r') as json_values:
    mdft_values = json.load(json_values)
    for value in mdft_values:
        values_label[value] = mdft_values[value]['label']


plots_dir = mdft_json[:-5]+"_plots"
os.mkdir(plots_dir)
plotter = mP.MdftPlotter(mdft_db, plots_dir)


for plot in plots_vs:
    for value in plots_vs[plot]['y'].split():
        plotter.plotVS(plots_vs[plot]['x'], value, values_label[plots_vs[plot]['x']], values_label[value], unit)
        
for plot in plots_errdistrib:
    values_list = plots_errdistrib[plot]['y'].split()
    plotter.plotErrorDistribution(plotter.calcDiffs(plots_errdistrib[plot]['x'], values_list, values_label[plots_errdistrib[plot]['x']], values_label), plots_errdistrib[plot]['filename'])

for plot in plots_by:
    values_list = plots_by[plot]['y'].split()
    plotter.plotErrorby(plotter.calcErrorby(plots_by[plot]['x'], values_list, values_label, plots_by[plot]['cat_column']), plots_by[plot]['cat_column']) 
    plotter.plotPbiasby(plotter.calcPbiasby(plots_by[plot]['x'], values_list, values_label, plots_by[plot]['cat_column']), plots_by[plot]['cat_column'])
    
os.system("cp " + mdft_json + " ./"+plots_dir)
