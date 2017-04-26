import os
import mdft_parser.parserJson as pJ
import mdft_parser.parserLog as pL
import mdft_writer.jsonWriter as jW
import mdft_parser.converter as cv

json_file = "mobley.json"

pJson = pJ.ParserJson()
pLog = pL.ParserLog()
converter = cv.Converter()

solute_dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

mdft_database = {}

for solute_dir in solute_dirs:
	for mdft_file in os.listdir(solute_dir):
		if mdft_file[-4:] == ".out":
			log_file = mdft_file
			pJson.parseData(json_file, solute_dir)
			pLog.parse(solute_dir+'/'+log_file)
			data_solute = pJson.getData()
            ### All quantities in kcal/mol
			if pLog.getMdftEnergy() != 'NaN':
				data_solute['mdft_energy'] = converter.kjTokcal(float(pLog.getMdftEnergy()))
				data_solute['delta_omega'] = converter.kjTokcal(float(pLog.getFunctionalAtMin()))
				data_solute['mdft_energy_pc'] = converter.kjTokcal(float(pLog.getMdftEnergyPc()))
				data_solute['mdft_energy_pc+'] = converter.kjTokcal(float(pLog.getMdftEnergyPcPlus()))
				#data_solute['mdft_energy_pmv'] = converter.kjTokcal(float(pLog.getMdftEnergyPmv()))
				#data_solute['mdft_energy_pid'] = converter.kjTokcal(float(pLog.getMdftEnergyPid()))
				mdft_database[solute_dir] = data_solute
			else:
				pass
			print solute_dir

newJson = jW.JsonWriter(mdft_database)
newJson.write('mdft.json')






























