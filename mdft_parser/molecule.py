class Molecule():
    def __init__(self, name = '', data = {}):
        self.name = name
        self.list_atoms = []
        self.data = {}
        
    def setName(self,name):
        self.name = name
        
    def addAtom(self, atome):
        self.list_atoms.append(atome)
    
    def setData(self, data):
		self.data = data
        
    def getListAtoms(self):
        return self.list_atoms

    def getName(self):
        return self.name

    def getData(self):
		return self.data

    def getNumberOfAtoms(self):
        return len(self.list_atoms)
    
    def __str__(self):
        return "<Molecule " + self.name + " with " + str(self.getNumberOfAtoms()) + " >"
    
        
