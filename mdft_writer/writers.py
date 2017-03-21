import os

def writeSoluteIn(fold, systeme, exp_dg, calc_dg, l_num, l_charge, l_sigma, l_epsilon, l_atomname, l_x, l_y, l_z, l_mass):
    with open(os.path.join(fold, "solute.in"), 'w') as solutein:
        solutein.write(systeme + '\t' + calc_dg +  '\t' + exp_dg + "\t#systeme  DGsolv_calc  DGsolv_expt (kJ/mol)" + '\n')
        #solutein.write("solute" + '\n')
        solutein.write(str(len(l_num)) + '\n')
        solutein.write("{0}    {1:10s}{2:10s}  {3:10s}  {4:10s}{5:10s}{6:9s}{7}\n".format("#","charge", "sigma(Ang)", "epsilon(kJ/mol)", "x", "y", "z", "Zatomic"))
        for i in xrange(len(l_num)):
            solutein.write("{0}{1:10.6f}{2:10.5f}{3:10.5f}{4:18.3f}{5:10.3f}{6:10.3f}{7:10d}\n".format(l_num[i], l_charge[i], l_sigma[l_atomname[i]], l_epsilon[l_atomname[i]], l_x[i], l_y[i],  l_z[i],  l_mass[i]))
            
            
def writeDftIn(fold,  l, n, mmax, temperature):
   with open(os.path.join(fold, "dft.in"), 'w') as dftin:
        dftin.write("boxnod = {0} {1} {2}".format(n,n,n) + '\n')
        dftin.write("boxlen = {0} {1} {2}".format(float(l),float(l),float(l)) + '\n')
        dftin.write("mmax = " + str(mmax) + "\n")
        dftin.write("temperature = " + str(temperature) + "\n") 
        
        
        
def writeDoFile(fold):
    with open(os.path.join(fold, "script.do"), 'w') as doFile:
        doFile.write("./mdft-dev")
        
