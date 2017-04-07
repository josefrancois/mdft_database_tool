import pandas as pd
import os
import mdft_analysis.mdftPlotter as mP

os.mkdir("mdft_plots")

mdft_db = pd.read_json("mdft.json", orient="index")

expt_label = "Experimental SFE (kcal/mol)"
calc_label = "Calculated SFE (kcal/mol)"
mdft_label = "MDFT estimated SFE (kcal/mol)"
mdft_pc_label = "PC MDFT SFE (kcal/mol)"
mdft_pc_plus_label = "PC+ MDFT SFE (kcal/mol)"
mdft_funcmin_label = "Functional at minimum (kcal/mol)"
mdft_label = {'calc': calc_label, 'expt':expt_label, 'mdft_energy':mdft_label,\
              'mdft_energy_pc':mdft_pc_label, 'mdft_energy_pc+':mdft_pc_plus_label, 'functional_at_min':mdft_funcmin_label}

plotter = mP.MdftPlotter(mdft_db)
for column in ['mdft_energy', 'mdft_energy_pc', 'mdft_energy_pc+', 'functional_at_min']:    
    plotter.plotVS('expt', column, expt_label, mdft_label[column])
    plotter.plotVS('calc', column, calc_label, mdft_label[column])
    
plotter.plotVS('expt', 'calc', expt_label, calc_label)

os.system("cp mdft.json ./mdft_plots")

###########
###### PLOTTING PROBLEMS !!!!! ==> All points are under bisector with MDFT quantities and we dunno why...
###########
