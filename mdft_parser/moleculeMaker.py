class Molecule():
    def __init__(self, name = '', list_atoms = [],  exp_dg = '', calc_dg = ''):
        self.list_atoms = list_atoms
        self.numberOfAtoms = len(list_atom)
        self.exp_dg = exp_dg
        self.calc_dg = calc_dg
        
    def setName(self,name):
        self.name = name
        
    def addAtom(self, atome):
        self.list_atoms.append(atome)
    
    def setExpDg(self, exp_dg):
        self.exp_dg = exp_dg
        
    def setCalcDg(self, calc_dg):
        self.calc_dg = calc_dg
        
	def getMolecule(self):
		return self.list_atoms
		
	def getName(self):
		return self.name
		
	def getExpDg(self):
		return self.exp_dg
	
	def getCalcDg(self):
		return self.calc_dg
		
	def getNumberofAtoms(self):
			return numberOfAtoms
    
        
