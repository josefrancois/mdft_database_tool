class Molecule():
    def __init__(self, name = '', list_atom = [], numatom = {}, exp_dg = '', calc_dg = ''):
        self.name = name
        self.molecule = list_atom
        self.exp_dg = exp_dg
        self.calc_dg = calc_dg
        
    def setName(self,name):
        self.name = name
        
    def addAtom(self, atome):
        self.molecule.append(atome)
    
    def setExpDg(self, exp_dg):
        self.exp_dg = exp_dg
        
    def setCalcDg(self, calc_dg):
        self.calc_dg = calc_dg
        
	def getMolecule(self):
		return self.molecule
		
	def getName(self):
		return self.name
		
	def getExpDg(self):
		return self.exp_dg
	
	def getCalcDg(self):
		return self.calc_dg
    
        
