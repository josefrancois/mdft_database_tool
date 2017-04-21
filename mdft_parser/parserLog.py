class ParserLog:
    "Definition of a MDFT output files parser"
	def __init__(self):
		self.mdft_energy = ''
		self.functional_at_min = ''
		self.mdft_energy_pc = ''
		self.mdft_energy_pc_plus = ''
		self.mdft_energy_pmv = ''
		self.mdft_energy_pid = ''
		
	def parse(self, logfile):
		with open(logfile, 'r') as flog :
			for line in flog:
				if "ENERGY" in line:
					self.mdft_energy = line.split()[-1]
				elif "Functional at min" in line:
					self.functional_at_min = line.split()[-2]
				elif "PC " in line:
					self.mdft_energy_pc = line.split()[-2]
				elif "PC+" in line:
					self.mdft_energy_pc_plus = line.split()[-2]
				elif "PMV" in line:
					self.mdft_energy_pmv = line.split()[-2]
				elif "Pid" in line:
					self.mdft_energy_pid = line.split()[-2]
					
					
	def getMdftEnergy(self):
		return self.mdft_energy
		
	def getFunctionalAtMin(self):
		return self.functional_at_min
		
	def getMdftEnergyPc(self):
		return self.mdft_energy_pc
		
	def getMdftEnergyPcPlus(self):
		return self.mdft_energy_pc_plus
	
	def getMdftEnergyPmv(self):
		return self.mdft_energy_pmv
	
	def getMdftEnergyPid(self):
		return self.mdft_energy_pid
