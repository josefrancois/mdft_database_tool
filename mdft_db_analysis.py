import pandas as pd
import os
import mdft_analysis.mdftPlotter as mP
import json
import argparse

arg_parser = argparse.ArgumentParser(prog="mdft_db_analysis.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--json", help = "JSON file to parse", default = "mdft.json")
mdft_args = arg_parser.parse_args()

mdft_db = pd.read_json(mdft_args.json, orient='index')

print mdft_db.shape[0], "solutes"

plots_vs = {}
plots_errdistrib = {}
plots_errgroups = {}
unit = ''
with open("references/parameters/mdftPlotConfig.json", 'r') as json_plots:
    plots = json.load(json_plots)
    plots_vs = plots['plotvs']
    plots_errdistrib = plots['errordistrib']
    plots_errgroups = plots['errorgroups']
    unit = plots['unit']


values_label = {}    
with open("references/parameters/mdftParsedValues.json", 'r') as json_values:
    values = json.load(json_values)
    for value in values:
        values_label[value] = values[value]['label']


plots_dir = mdft_args.json[:-5]+"_plots"
os.mkdir(plots_dir)
plotter = mP.MdftPlotter(mdft_db, plots_dir)


for plot in plots_vs:
    for value in plots_vs[plot]['y'].split():
        if plots_vs[plot]['x_label'] not in values_label:
            values_label[plots_vs[plot]['x']] = plots_vs[plot]['x_label']
        plotter.plotVS(plots_vs[plot]['x'], value, plots_vs[plot]['x_label'], values_label[value], unit)
        
for plot in plots_errdistrib:
    values_list = plots_errdistrib[plot]['comp'].split()
    plotter.plotErrorDistribution(plotter.calcDiffs(plots_errdistrib[plot]['ref'], values_list, plots_errdistrib[plot]["ref_label"], values_label), plots_errdistrib[plot]['name'])

for plot in plots_errgroups:
    values_list = plots_errgroups[plot]['y'].split()
    plotter.plotErrorGroups(plotter.calcErrorGroups(plots_errgroups[plot]['x'], values_list, values_label)) 
    
os.system("cp " + mdft_args.json + " ./"+plots_dir)

