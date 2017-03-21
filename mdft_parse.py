import os
import json

dico_mdft = {}
for elt in os.listdir("./mdft-log"):
    solute = elt[elt.find("_")+1:]
    with open(os.path.join("./mdft-log/output_"+solute, solute+".log"), 'r') as f:     
        for l in f:
            if l.find("ENERGY") != -1:
                dico_mdft[solute] = float(l.split()[-1])



with open("mobley.json", 'r') as json_file:
    mobley_db = json.load(json_file)
    for elt in mobley_db.keys():
        if mobley_db[elt]["iupac"] in dico_mdft.keys():
            mobley_db[elt]["calc_mdft"] = dico_mdft[mobley_db[elt]["iupac"]]
       
with open("mobley_mdft.json", 'w') as mobley_mdft:
    json.dump(mobley_db, mobley_mdft, indent = 4)








