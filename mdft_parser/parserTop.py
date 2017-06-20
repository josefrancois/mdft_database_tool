import converter as cv

class ParserTop:
    "Definition of a parser for GROMACS .top files to get the needed infos about the atoms"  
    def __init__(self):
        self.list_name = []
        self.list_atomtype = []
        self.list_charge = []
        self.list_numatom = []
        self.list_num = []
        self.list_sigma = {}
        self.list_epsilon = {}
        
    def parseAtoms(self, ftop):
        with open(ftop, 'r') as top:
            lines = top.readlines() 
            converter = cv.Converter()
            #print lines        
            for ind, line in enumerate(lines):
                if ind > lines.index('[ atoms ]\n') and ind < lines.index('[ bonds ]\n'):
                    if len(line) < 2 or line[0] == ';': #avoid commentaries and blank line
                        continue
                    else:
                        self.list_name.append(line.split()[4])
                        self.list_num.append(line.split()[0])
                        self.list_atomtype.append(line.split()[1])
                        self.list_charge.append(float(line.split()[6]))
                        self.list_numatom.append(int(round(float(line.split()[7])/2)))     
                elif ind > lines.index('[ atomtypes ]\n') and ind < lines.index('[ moleculetype ]\n'):
                    #print line
                    if len(line) < 2 or line[0] == ';': #avoid commentaries and blank line
                        continue
                    else :
                        self.list_sigma[line[0:10].strip()] = converter.nmToangstrom(float(line[42:59].strip()))
                        self.list_epsilon[line[0:10].strip()] = float(line[59:73].strip())
                    
    def getNumberOfAtoms(self):
        return len(self.list_name)
    
    def getListName(self):
        return self.list_name
        
    def getListAtomtype(self):
        return self.list_atomtype
        
    def getListCharge(self):
        return self.list_charge
        
    def getListNumatom(self):
        return self.list_numatom
        
    def getListNum(self):
        return self.list_num
        
    def getListSigma(self):
        return self.list_sigma
        
    def getListEpsilon(self):
        return self.list_epsilon
