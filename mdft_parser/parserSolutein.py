from atom import *
from molecule import *

class SoluteinParser:
    "Defines a solute.in parser"
    def __init__(self):
        self.name = ''
        self.list_num = []
        self.list_x = []
        self.list_y = []
        self.list_z = []
        self.list_atomtype = []
        self.list_charge = []
        self.list_numatom = []
        self.list_sigma = []
        self.list_epsilon = []
        
    def parse(self, solutein):
        with open(solutein, 'r') as sltin:
            for ind, line in enumerate(sltin):
                if ind == 0:
                    self.name = line.split()[0] # Name of the molecule
                if ind >= 3: # Parsing of informations about the atoms composing the molecule
                     self.list_num.append(line.split()[0])
                     self.list_charge.append(float(line.split()[1]))
                     self.list_sigma.append(float(line.split()[2]))
                     self.list_epsilon.append(float(line.split()[3]))
                     self.list_x.append(float(line.split()[4]))
                     self.list_y.append(float(line.split()[5]))
                     self.list_z.append(float(line.split()[6]))
                     self.list_numatom.append(line.split()[7])
    
    def getName(self):
        return self.name
                         
    def getListNum(self):
        return self.list_num
        
    def getListx(self):
        return self.list_x
        
    def getListy(self):
        return self.list_y
        
    def getListz(self):
        return self.list_z
        
    def getListAtomtype(self):
        return self.list_atomtype
        
    def getListCharge(self):
        return self.list_charge
        
    def getListNumatom(self):
        return self.list_numatom
            
    def getListSigma(self):
        return self.list_sigma
        
    def getListEpsilon(self):
        return self.list_epsilon
    
    def getNumberOfAtoms(self):
        return len(self.list_num) 
