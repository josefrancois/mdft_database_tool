class dftIn:
    def __init__(self):
        self.l = 0.0
        self.n = 0
        self.mmax = 1
        self.temperature = 298.15
        

    def writeDftIn(self.l, self.n):
       with open("dft.in", 'w') as dftin:
            dftin.write("boxnod = {0} {1} {2}".format(self.n,self.n,self.n) + '\n')
            dftin.write("boxlen = {0} {1} {2}".format(float(self.l),float(self.l),float(self.l)) + '\n')
            dftin.write("mmax = " + str(self.mmax) + "\n")
            dftin.write("temperature = " + str(self.temperature) + "\n")                          
