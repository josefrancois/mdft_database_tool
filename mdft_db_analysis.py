import pandas as pd
import os
import mdft_analysis.mdftPlotter as mP
import json

os.mkdir("mdft_plots")
mdft_db = pd.read_json("mdft.json", orient="index")

mdft_plots = {}
unit = ''
with open("references/parameters/mdftPlotConfig.json", 'r') as json_plots:
    plots = json.load(json_plots)
    mdft_plots = plots['list']
    unit = plots['unit']

plotter = mP.MdftPlotter(mdft_db)
for plot in mdft_plots:
    plotter.plotVS(mdft_plots[plot]['x'], mdft_plots[plot]['y'], mdft_plots[plot]['x_label'], mdft_plots[plot]['y_label'], unit, mdft_plots[plot]['title'])
    

os.system("cp mdft.json ./mdft_plots")

###########
###### PLOTTING PROBLEMS !!!!! ==> All points are under bisector with MDFT quantities and we dunno why...
###########
