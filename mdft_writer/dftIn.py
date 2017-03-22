class dftIn:
	self.mmax = 1
    self.temperature = 298.15
    
    def __init__(self, l=32.0, n=64, solvent=None):
        self.l = l
        self.n = n
        self.solvent = solvent

    def writeDftIn(self):
       with open("dft.in", 'w') as dftin:
            dftin.write("boxnod = {0} {1} {2}".format(self.n,self.n,self.n) + '\n')
            dftin.write("boxlen = {0} {1} {2}".format(float(self.l),float(self.l),float(self.l)) + '\n')
            dftin.write("mmax = " + str(self.mmax) + "\n")
            dftin.write("temperature = " + str(self.temperature) + "\n")                          
			if (self.solvent is not None) :
				dftin.write("solvent = " + str(self.solvent) + "\n")                          


    @classmethod
    def setMmax(self, mmax):
		self.mmax=mmax

    @classmethod
    def setTemperature(self, temperature):
		self.temperature=temperature

    def setN(self, n):
		if(n>0):
			self.n = n
		
    def setL(self, l):
		if(l>0.0):
			self.l = l
		
    def setSolvent(self, solvent):
		self.solvent = solvent

    @classmethod
    def getMmax(self):
		return self.mmax

    @classmethod
    def getTemperature(self):
		return self.temperature

    def getN(self, n):
		return self.n
			
    def getL(self):
		return self.l
			
    def getSolvent(self):
		return self.solvent
