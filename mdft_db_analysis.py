import pandas as pd
import os
import mdft_analysis.mdftPlotter as mP
import json
import argparse

arg_parser = argparse.ArgumentParser(prog="mdft_db_analysis.py", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument("--json", help = "JSON file to parse", default = "mdft.json")
mdft_args = arg_parser.parse_args()


mdft_db = pd.read_json(mdft_args.json, orient="index")
plots_dir = mdft_args.json[:-5]+"_plots"
os.mkdir(plots_dir)

mdft_plots = {}
unit = ''
with open("references/parameters/mdftPlotConfig.json", 'r') as json_plots:
    plots = json.load(json_plots)
    mdft_plots = plots['list']
    unit = plots['unit']

plotter = mP.MdftPlotter(mdft_db, plots_dir)
for plot in mdft_plots:
    plotter.plotVS(mdft_plots[plot]['x'], mdft_plots[plot]['y'], mdft_plots[plot]['x_label'], mdft_plots[plot]['y_label'], unit, mdft_plots[plot]['title'])
    plotter.plotEnrichmentCurve(mdft_plots[plot]['x'], mdft_plots[plot]['y'])
    

os.system("cp " + mdft_args.json + " ./"+plots_dir)

