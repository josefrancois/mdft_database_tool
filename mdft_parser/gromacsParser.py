from atom import *
from molecule import *
from parserTop import *
from parserGro import *
from parserJson import *

def parse(grofile, topfile, jsonfile):
    gro = ParserGro()
    top = ParserTop()
    fjson = ParserJson()
    
    gro.parseCoord(grofile)
    top.parseAtoms(topfile)
    fjson.parseEnergies(jsonfile)
    
    atom = Atom()
    molecule = Molecule()
    
    for i in range(parserGro.getNumberOfAtoms):
        atom.setAtomtype(top.list_atomtype[i])
        atom.setCoord(gro.list_x[i], gro.list_y[i], gro.list_z[i])
        atom.setNum(top.list_num[i])
        atom.setCharge(top.list_charge[i])
        atom.setNumatom(top.list_numatom[i])
        atom.setSigma(top.list_sigma[list_atomname[i]])
        atom.setEspilon(top.list_epsilon[list_atomname[i]])
        molecule.addAtom(atom)   
    return molecule
        
