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

plots_dir = mdft_args.json[:-5]+"_plots"
os.mkdir(plots_dir)

mdft_plots = {}
unit = ''

with open("references/parameters/mdftPlotConfig.json", 'r') as json_plots:
    plots = json.load(json_plots)
    mdft_plots = plots['list']
    unit = plots['unit']
    
label_list_expt = []
label_list_calc = []

mdft_db_diff_expt = pd.DataFrame()
mdft_db_diff_calc = pd.DataFrame()

plotter = mP.MdftPlotter(mdft_db, plots_dir)

for plot in mdft_plots:
    plotter.plotVS(mdft_plots[plot]['x'], mdft_plots[plot]['y'], mdft_plots[plot]['x_label'], mdft_plots[plot]['y_label'], unit, mdft_plots[plot]['title'])
    #plotter.plotEnrichmentCurve(mdft_plots[plot]['x'], mdft_plots[plot]['y'])    
    diff = mdft_db[mdft_plots[plot]['y']]-mdft_db[mdft_plots[plot]['x']]
    if mdft_plots[plot]['x'] == 'expt' and mdft_plots[plot]['y'] not in ['mdft_energy', 'delta_omega'] :
        mdft_db_diff_expt = pd.concat([mdft_db_diff_expt, diff], axis=1)
        label_list_expt.append(mdft_plots[plot]['y_label']+' - '+mdft_plots[plot]['x_label'])
    elif mdft_plots[plot]['x'] == 'calc' and mdft_plots[plot]['y'] not in ['mdft_energy', 'delta_omega'] :
        mdft_db_diff_calc = pd.concat([mdft_db_diff_calc, diff], axis=1)
        label_list_calc.append(mdft_plots[plot]['y_label']+' - '+mdft_plots[plot]['x_label'])
        
mdft_db_diff_expt.columns = label_list_expt
mdft_db_diff_calc.columns = label_list_calc

plotter.plotErrorDistribution(mdft_db_diff_expt, "err_distrib_expt")
plotter.plotErrorDistribution(mdft_db_diff_calc, "err_distrib_calc")

os.system("cp " + mdft_args.json + " ./"+plots_dir)

