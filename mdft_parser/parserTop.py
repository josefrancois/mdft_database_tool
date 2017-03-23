class ParserTop:  
	def __init__(self):
		self.list_name = []
		self.list_atomtype = []
		self.list_charge = []
		self.list_numatom = [] 
		self.list_num = []
		self.list_sigma = {}
		self.list_epsilon = {}
		self.number_of_atoms = len(self.list_name)
        
	def parseAtoms(self, ftop):                                                                
		with open(ftop, 'r') as top:         
			for line in top:
				if line.find('MOL') != -1:
					self.list_name.append(line.split()[4])
					self.list_num.append(line.split()[0])
					self.list_atomtype.append(line.split()[1])
					self.list_charge.append(float(line.split()[6]))
					self.list_numatom.append(int(round(float(line.split()[7])/2)))
				elif line.find('  A  ') != -1:
					self.list_sigma[line.split()[0]] = float(line.split()[5])*10
					self.list_epsilon[line.split()[0]] = float(line.split()[6])* 4.187      
					
	def getNumberOfAtoms(self):
		return self.number_of_atoms
