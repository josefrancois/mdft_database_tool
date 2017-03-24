import json

class ParserJson:  
    def __init__(self, solute_name = '', data_solute = {}):
        self.solute_name = solute_name
        self.data_solute = {}

    def parseData(self, fjson, name):
        self.solute_name = name        
        with open(fjson, 'r') as json_file:            
            solute_db = json.load(json_file)
            self.data_solute = solute_db[self.solute_name]    

    def getSoluteName(self):
        return self.solute_name
        
    def getDataSolute(self):
        return self.data_solute
    
