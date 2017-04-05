import pandas as pd

import mdft_analysis.mdftPlotter as mP


mdft_db = pd.read_json("mdft.json", orient="index")
mdft_db["mdft_energy_kcalmol"] = mdft_db["mdft_energy"]*0.239006

expt_label = "Experimental SFE (kcal/mol)"
calc_label = "Calculated SFE (kcal/mol)"
mdft_label = "MDFT estimated SFE (kcal/mol)"
plotter1 = mP.MdftPlotter(mdft_db)
plotter2 = mP.MdftPlotter(mdft_db)
plotter3 = mP.MdftPlotter(mdft_db)

plotter1.plotVS('expt', 'calc', expt_label, calc_label)
plotter2.plotVS('expt', 'mdft_energy_kcalmol', expt_label, mdft_label)
plotter3.plotVS('calc', 'mdft_energy_kcalmol', calc_label, mdft_label)

