import json

class ParserJson:
    "Definition of a parser for JSON files"  
    def __init__(self, record = '', data_record = {}):
        self.record = record
        self.data_record = {}

    def parseData(self, fjson, record_name):
        #Parse the data about the record 'record_name' in the JSON file 'fjson' 
        self.record = record_name        
        with open(fjson, 'r') as json_file:            
            json_db = json.load(json_file)
            self.data_record = json_db[self.record]    

    def getRecordName(self):
        return self.record
        
    def getData(self):
        return self.data_record
    
