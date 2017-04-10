import converter as cv

class ParserGro:  
    def __init__(self, list_x = [], list_y = [], list_z = []):
        self.list_x = list_x
        self.list_y = list_y
        self.list_z = list_z
        
    def parseCoord(self, fgro): 
        converter = cv.Converter()       
        with open(fgro, 'r') as gro:  
            for line in gro:
                if line.find("MOL") != -1:
                    self.list_x.append(converter.nmToangstrom(float(line.split()[4])))
                    self.list_y.append(converter.nmToangstrom(float(line.split()[5])))
                    self.list_z.append(converter.nmToangstrom(float(line.split()[6])))
                    
    def getListx(self):
        return self.list_x
        
    def getListy(self):
        return self.list_y
        
    def getListz(self):
        return self.list_z
