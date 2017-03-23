from dftInWriter import *
from soluteInWriter import *


def writeMdftFiles(folder, molecule):
	solutein = SoluteInWriter(molecule)
	dftin = DftInWriter()
	
	solutein.write(folder)
	dftin.write(folder)
