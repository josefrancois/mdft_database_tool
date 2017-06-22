import os


class DftInWriter:
    "Definition of a dft.in file writer for MDFT"
    def __init__(self):
        self.l = {'x': None, 'y': None, 'z': None}
        self.n = {'x': None, 'y': None, 'z': None}
        self.mmax = None
        self.temperature = None
        self.solvent = None
        self.bridge = None
        self.scsf = None
        self.dss = None
        
    def write(self, folder):
        with open(os.path.join(folder, "dft.in"), 'w') as dftin:
            dftin.write("boxnod = {0} {1} {2}".format(self.n['x'],self.n['y'],self.n['z']) + '\n')
            dftin.write("boxlen = {0} {1} {2}".format(float(self.l['x']),float(self.l['y']),float(self.l['z'])) + '\n')
            dftin.write("mmax = " + str(self.mmax) + "\n")
            dftin.write("temperature = " + str(self.temperature) + "\n")  
            dftin.write("bridge = " + str(self.bridge) + "\n")
            dftin.write("solute_charges_scale_factor = " + str(self.scsf) + "\n")
            dftin.write("direct_solute_sigmak = " + str(self.dss) + "\n")                        
            if (self.solvent is not None) :
                dftin.write("solvent = " + str(self.solvent) + "\n")                          

    def setMmax(self, mmax):
        self.mmax=mmax

    def setTemperature(self, temperature):
        self.temperature=temperature
        
    def setNx(self, nx):
        if(nx>0.0):
            self.n['x'] = nx
            
    def setNy(self, ny):
        if(ny>0.0):
            self.n['y'] = ny
            
    def setNz(self, nz):
        if(nz>0.0):
            self.n['z'] = nz
            
    def setLx(self, lx):
        if(lx>0.0):
            self.l['x'] = lx
            
    def setLy(self, ly):
        if(ly>0.0):
            self.l['y'] = ly
            
    def setLz(self, lz):
        if(lz>0.0):
            self.l['z'] = lz
        
    def setSolvent(self, solvent):
        self.solvent = solvent
        
    def setBridge(self, bridge):
        self.bridge = bridge
        
    def setSCSF(self, scsf):#scsf => Solute charges scale factor
        self.scsf = scsf
        
    def setDSS(self, dss):#dss => Direct Solute Sigma k
        self.dss = dss

    def getMmax(self):
        return mmax

    def getTemperature(self):
        return temperature
               
    def getNx(self):
        return self.l['x']
        
    def getNy(self):
        return self.l['y']
        
    def getNz(self):
        return self.l['z']
            
    def getLx(self):
        return self.l['x']
        
    def getLy(self):
        return self.l['y']
        
    def getLz(self):
        return self.l['z']
            
    def getSolvent(self):
        return self.solvent
    
    def getBridge(self):
        return self.bridge
        
    def getSCSF(self):
        return self.scsf
    
    def getDSS(self, dss):
        return self.dss
