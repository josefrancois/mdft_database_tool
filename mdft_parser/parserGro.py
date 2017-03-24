class ParserGro:  
    def __init__(self, list_x = [], list_y = [], list_z = []):
        self.list_x = list_x
        self.list_y = list_y
        self.list_z = list_z
        
    def parseCoord(self, fgro):        
        with open(fgro, 'r') as gro:  
            for line in gro:
                if line.find("MOL") != -1:
                    self.list_x.append(float(line.split()[4])*10)
                    self.list_y.append(float(line.split()[5])*10)
                    self.list_z.append(float(line.split()[6])*10) 
                    
    def getListx(self):
        return self.list_x
        
    def getListy(self):
        return self.list_y
        
    def getListz(self):
        return self.list_z
