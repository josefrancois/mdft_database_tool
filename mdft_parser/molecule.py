class Molecule():
    def __init__(self, name = '', data = {}, wth = 0.0):
        self.name = name
        self.list_atoms = []
        self.data = {}
        self.width = 0.0 
        
    def setName(self,name):
        self.name = name
        
    def addAtom(self, atome):
        self.list_atoms.append(atome)
    
    def setData(self, data):
        self.data = data
        
    def setWidth(self, width):
        self.width = width
        
    def getListAtoms(self):
        return self.list_atoms

    def getName(self):
        return self.name

    def getData(self):
        return self.data
    
    def getWidth(self):
        return self.width

    def getNumberOfAtoms(self):
        return len(self.list_atoms)
    
    def __str__(self):
        return "<Molecule " + self.name + " with " + str(self.getNumberOfAtoms()) + " >"
    
        
