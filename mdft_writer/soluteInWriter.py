import os

class SoluteInWriter:
	def __init__(self, molecule = None):
		self.molecule = molecule
                      
	def write(self, folder):
		print self.molecule.name
		with open(os.path.join(folder, "solute.in"), 'w') as solutein:
			solutein.write(self.molecule.name + '\t' + self.molecule.calc_dg +  '\t' + self.molecule.exp_dg + "\t#systeme  DGsolv_calc (kJ/mol)  DGsolv_expt (kJ/mol)" + '\n')
			#solutein.write("solute" + '\n')
			solutein.write(str(self.number_of_atoms) + '\n')
			solutein.write("{0:10s}{1:10s}{2:10s}{3:10s}{4:10s}{5:10s}{6:9s}{7}\n"\
			.format("#","charge", "sigma(Ang)", "epsilon(kJ/mol)", "x", "y", "z", "Zatomic"))
			for atom in self.list_atoms:
				solutein.write("{0:10s}{1:10.6f}{2:10.5f}{3:10.5f}{4:18.3f}{5:10.3f}{6:10.3f}{7:10d}\n"\
				.format(atom.num, atom.charge, atom.epsilon, atom.coord['x'], atom.coord['y'], atom.coord['z'], atom.numatm))
