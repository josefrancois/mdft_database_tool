import json
import converter as cv
import math as m

class ParserLog:
    "Definition of a MDFT output files parser"
    def __init__(self):
        with open('references/parameters/mdftParsedValues.json' , 'r') as fjson:
            self.mdft_values = json.load(fjson) 
        
    def parse(self, logfile):
        data_log = {}
        converter = cv.Converter()
	with open(logfile, 'r') as flog :
            for line in flog:
                for mdft_value in self.mdft_values:
                    #To avoid any decoding error from 'mdftParsedValues.json' file reading AND avoid all 'NaN' results
                    if self.mdft_values[mdft_value]['flag'].encode('ascii', 'ignore') in line and m.isnan(float(line.split()[self.mdft_values[mdft_value]['position']]))==False:         
		                # All quantities in kcal/mol
                        data_log[mdft_value] = converter.kjTokcal(float(line.split()[self.mdft_values[mdft_value]['position']]))
			
        	
	    return data_log
