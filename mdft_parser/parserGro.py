class ParserGro:  
    def __init__(self):
        self.list_x = []
        self.list_y = []
        self.list_z = []
        
    def parseCoord(self, fgro):        
        with open(fgro, 'r') as gro:  
            for line in gro:
                if line.find("MOL") != -1:
                    self.list_x.append(float(line.split()[4])*10)
                    self.list_y.append(float(line.split()[5])*10)
                    self.list_z.append(float(line.split()[6])*10) 
                    
    def getNumberofAtoms(self):
        return len(self.list_x)   
