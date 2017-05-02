import simplejson as json
import converter as cv

class ParserLog:
    "Definition of a MDFT output files parser"
    def __init__(self):
        with open('references/parameters/mdftParsedValues.json' , 'r') as fjson:
            self.mdft_values = json.load(fjson)
            
            
        #self.mdft_energy = ''
        #self.functional_at_min = ''
        #self.mdft_energy_pc = ''
        #self.mdft_energy_pc_plus = ''
        #self.mdft_energy_pmv = ''
        #self.mdft_energy_pid = ''
        
    def parse(self, logfile):
        data_log = {}
        converter = cv.Converter()
        with open(logfile, 'r') as flog :
            for line in flog:
                for mdft_value in self.mdft_values:
                    if self.mdft_values[mdft_value]['flag'] in line:
                        ### All quantities in kcal/mol
                        data_log[mdft_value] = converter.kjTokcal(float(line.split()[self.mdft_values[mdft_value]['position']]))
        return data_log
