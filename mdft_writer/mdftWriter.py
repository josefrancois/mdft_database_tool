from dftInWriter import *
from soluteInWriter import *


class MdftWriter:
    "This class uses infos from parsers and submitted parameters to write the wanted dft.in and solute.in files for each molecule"
    def __init__(self, molecule = None, parameters = {}):
        self.molecule = molecule
        self.parameters = parameters
        
        
    def write(self, folder):
        solutein = SoluteInWriter(self.molecule)
        dftin = DftInWriter()
        
        solutein.write(folder)
         
        dftin.setLx(int(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['x'])+1)
        dftin.setLy(int(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['y'])+1)
        dftin.setLz(int(2* self.parameters['lb'] + self.molecule.getMoleculeWidth()['z'])+1)

        dftin.setNx(int(dftin.getLx()/self.parameters['dx']))
        dftin.setNy(int(dftin.getLy()/self.parameters['dx']))
        dftin.setNz(int(dftin.getLz()/self.parameters['dx']))
                

        dftin.setSolvent(self.parameters['solvent'])

        dftin.setMmax(self.parameters['mmax'])

        dftin.setTemperature(self.parameters['temperature'])

        dftin.setBridge(self.parameters['bridge'])  
                
        dftin.write(folder)
