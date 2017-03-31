import mdft_analysis.mdftPlotter as mP
import json

y_expt = []
x_md = []
x_mdft = []

with open("mdft.json",'r') as json_file:
    mdft_db = json.load(json_file)    
    for elt in mdft_db:
        x_md.append(mdft_db[elt]["calc"])
        y_expt.append(mdft_db[elt]["expt"])

plotter = mP.MdftPlotter(x_md, y_expt)
plotter.plot("expt VS calc","calc", "expt") 

