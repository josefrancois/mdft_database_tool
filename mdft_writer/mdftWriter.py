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
         
        dftin.setLx(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['x'])
        dftin.setLy(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['y'])
        dftin.setLz(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['z'])

        dftin.setNx(int(dftin.getLx()/self.parameters['dx']))
        dftin.setNy(int(dftin.getLy()/self.parameters['dx']))
        dftin.setNz(int(dftin.getLz()/self.parameters['dx']))
                

        dftin.setSolvent(self.parameters['solvent'])

        dftin.setMmax(self.parameters['mmax'])

        dftin.setTemperature(self.parameters['temperature'])

        dftin.setBridge(self.parameters['bridge'])  
                
        dftin.write(folder)
