class Atom:
    "Definition of an atom by its name, number, type, coordinates, charge, epsilon, sigma and atomic number"
    def __init__(self, name = '', num = 1, atype = '', coord = {'x':0.0, 'y':0.0, 'z':0.0},  q = 0.0, eps = 0.0, sig = 0.0, numatm = 1):
        self.name = name
        self.num = num
        self.atomtype = atype
        self.coord = coord      
        self.charge = q
        self.epsilon = eps
        self.sigma = sig
        self.numatm = numatm
        
    def setName(self, name):
        self.name = name
        
    def setNum(self, num):
        self.num = num
    
    def setAtomtype(self, atomtype):
        self.atomtype = atomtype
    
    def setCoord(self, x, y, z):
        self.coord = {'x':x, 'y':y, 'z':z}
    
    def setCharge(self, charge):
        self.charge = charge
        
    def setEpsilon(self, dict_epsilon):
        self.epsilon = dict_epsilon[self.atomtype]
    
    def setSigma(self, dict_sigma):
        self.sigma = dict_sigma[self.atomtype]
    
    def setNumatm(self, numatm):
        self.numatm = numatm
	
    def getName(self):
        return self.name
        
    def getNum(self):
        return self.num
    
    def getAtomtype(self):
        return self.atomtype
    
    def getCoord(self):
        return self.coord 
    
    def getCharge(self):
        return self.charge
        
    def getEpsilon(self):
        return self.epsilon
    
    def getSigma(self):
        return self.sigma
    
    def getNumatm(self):
        return self.numatm
