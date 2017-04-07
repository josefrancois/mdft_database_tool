import os
import mdft_parser.parserJson as pJ
import mdft_parser.parserLog as pL
import mdft_writer.jsonWriter as jW

json_file = "mobley.json"

pJson = pJ.ParserJson()
pLog = pL.ParserLog()

solute_dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

mdft_database = {}

for solute_dir in solute_dirs:
	for mdft_file in os.listdir(solute_dir):
		if mdft_file[-4:] == ".out":
			log_file = mdft_file
			pJson.parseData(json_file, solute_dir)
			pLog.parse(solute_dir+'/'+log_file)
			data_solute = pJson.getDataSolute()
			# ALL QUANTITIES IN KCAL/MOL !!!!!!!!
			data_solute['mdft_energy'] = float(pLog.getMdftEnergy())*0.239006
			data_solute['functional_at_min'] = float(pLog.getFunctionalAtMin())*0.239006
			data_solute['mdft_energy_pc'] = float(pLog.getMdftEnergyPc())*0.239006
			data_solute['mdft_energy_pc+'] = float(pLog.getMdftEnergyPcPlus())*0.239006
			data_solute['mdft_energy_pmv'] = float(pLog.getMdftEnergyPmv())*0.239006
			data_solute['mdft_energy_pid'] = float(pLog.getMdftEnergyPid())*0.239006
			print solute_dir
			mdft_database[solute_dir] = data_solute

newJson = jW.JsonWriter(mdft_database)
newJson.write('mdft.json')






























