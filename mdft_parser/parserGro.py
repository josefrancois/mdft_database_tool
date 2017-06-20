import converter as cv

class ParserGro:
    "Definition of a parser for GROMACS .gro files to retrieve the atom coordintates"  
    def __init__(self):
        self.list_x = []
        self.list_y = []
        self.list_z = []
        
    def parseCoord(self, fgro):
        converter = cv.Converter() # => in order to convert from nm to angstrom for MDFT
        with open(fgro, 'r') as gro:  
            for ind, line in enumerate(gro):
                if ind >= 2 and len(line.split()) > 3:
                    self.list_x.append(converter.nmToangstrom(float(line[20:28].strip())))
                    self.list_y.append(converter.nmToangstrom(float(line[28:36].strip())))
                    self.list_z.append(converter.nmToangstrom(float(line[36:44].strip())))
                    
    def getListx(self):
        return self.list_x
        
    def getListy(self):
        return self.list_y
        
    def getListz(self):
        return self.list_z
