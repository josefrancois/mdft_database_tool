from dftInWriter import *
from soluteInWriter import *


class MdftWriter:
    def __init__(self, molecule = None, parameters = {}):
        self.molecule = molecule
        self.parameters = parameters
        
        
    def write(self, folder):
        solutein = SoluteInWriter(self.molecule)
        dftin = DftInWriter()
        
        solutein.write(folder)
         
        if self.parameters['L'] is not None:
            dftin.setL(self.parameters['L'])
        if self.parameters['N'] is not None:
            dftin.setN(self.parameters['N'])        
        if self.parameters['solvent'] is not None:
            dftin.setSolvent(self.parameters['solvent'])
        if self.parameters['mmax'] is not None:
            dftin.setMmax(self.parameters['mmax'])
        if self.parameters['temperature']is not None:
            dftin.setTemperature(self.parameters['temperature'])   
                
        dftin.write(folder)
