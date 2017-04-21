class Molecule():
    "Definition of a molecule by its name, list of atoms, data and its width"
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
        
    def getListAtoms(self):
        return self.list_atoms

    def getName(self):
        return self.name

    def getData(self):
        return self.data

    def getNumberOfAtoms(self):
        return len(self.list_atoms)
        
    def getMoleculeWidth(self):
        list_coord = {'x':[], 'y':[], 'z':[]}
        for i in xrange(len(self.list_atoms)):
            list_coord['x'].append(self.list_atoms[i].coord['x'])
            list_coord['y'].append(self.list_atoms[i].coord['y'])
            list_coord['z'].append(self.list_atoms[i].coord['z'])
        x_width = max(list_coord['x'])-min(list_coord['x'])
        y_width = max(list_coord['y'])-min(list_coord['y'])
        z_width = max(list_coord['z'])-min(list_coord['z'])
        molecule_width = {'x':x_width, 'y':y_width, 'z':z_width}
        return molecule_width
        
    def __str__(self):
        return "<Molecule " + self.name + " with " + str(self.getNumberOfAtoms()) + " >"
    
        
