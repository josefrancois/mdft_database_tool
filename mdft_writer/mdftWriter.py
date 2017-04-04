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
         
        if self.parameters['lb'] is not None:
            dftin.setL(2* self.parameters['lb'] + self.molecule.getWidth())
        if self.parameters['dx'] is not None:
            dftin.setN(int(dftin.getL()/self.parameters['dx']))        
        if self.parameters['solvent'] is not None:
            dftin.setSolvent(self.parameters['solvent'])
        if self.parameters['mmax'] is not None:
            dftin.setMmax(self.parameters['mmax'])
        if self.parameters['temperature']is not None:
            dftin.setTemperature(self.parameters['temperature'])   
                
        dftin.write(folder)
