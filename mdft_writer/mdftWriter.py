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
            dftin.setLx(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['x'])
            dftin.setLy(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['y'])
            dftin.setLz(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['z'])
        if self.parameters['dx'] is not None:
            dftin.setNx(int(dftin.getLx()/self.parameters['dx']))
            dftin.setNy(int(dftin.getLy()/self.parameters['dx']))
            dftin.setNz(int(dftin.getLz()/self.parameters['dx']))
                    
        if self.parameters['solvent'] is not None:
            dftin.setSolvent(self.parameters['solvent'])
        if self.parameters['mmax'] is not None:
            dftin.setMmax(self.parameters['mmax'])
        if self.parameters['temperature']is not None:
            dftin.setTemperature(self.parameters['temperature'])   
                
        dftin.write(folder)
