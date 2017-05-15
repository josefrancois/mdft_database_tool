import os

class SoluteInWriter:
    "Definition of a solute.in file writer"
    def __init__(self, molecule = None):
        self.molecule = molecule
                      
    def write(self, folder):
        with open(os.path.join(folder, "solute.in"), 'w') as solutein:
            solutein.write(self.molecule.getName() + '\n')
            solutein.write(str(self.molecule.getNumberOfAtoms()) + '\n')
            solutein.write("{0:8s}{1:10s}{2:15s}{3:20s}{4:10s}{5:10s}{6:9s}{7}\n"\
            .format("#","charge", "sigma(Ang)", "epsilon(kJ/mol)", "x", "y", "z", "Zatomic"))
            for atom in self.molecule.getListAtoms():
                solutein.write("{0}{1:10.6f}{2:10.6f}{3:20.6f}{4:10.3f}{5:10.3f}{6:10.3f}{7:10d}\n"\
                .format(atom.getNum(), atom.getCharge(), atom.getSigma(), atom.getEpsilon(), atom.getCoord()['x'], atom.getCoord()['y'], atom.getCoord()['z'], atom.getNumatm()))
