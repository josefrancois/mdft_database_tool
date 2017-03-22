class Molecule():
    def __init__(self, name = '', list_atom = [], numatom = {}, exp_dg = 0.0, calc_dg = 0.0):
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
    
        
