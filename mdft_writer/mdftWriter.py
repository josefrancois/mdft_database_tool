from dftInWriter import *
from soluteInWriter import *


class MdftWriter:
	def __init__(self, molecule = None):
		self.molecule = molecule

	def write(self, folder):
		solutein = SoluteInWriter(self.molecule)
		dftin = DftInWriter()
		
		solutein.write(folder)
		dftin.write(folder)
