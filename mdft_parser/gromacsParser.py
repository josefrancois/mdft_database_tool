from atom import *
from molecule import *
from parserTop import *
from parserGro import *
from parserJson import *


class GromacsParser:
    def __init__(self, gro_filename = '', top_filename = ''):
        self.gro_filename = gro_filename
        self.top_filename = top_filename


    def parse(self):
        gro = ParserGro()
        top = ParserTop()
        
        
        gro.parseCoord(self.gro_filename)
        top.parseAtoms(self.top_filename)
        molecule = Molecule()
        #print molecule
        
        for i in range(top.getNumberOfAtoms()):
            #print top.getListName()[i]
            atomtype = top.getListAtomtype()[i]
            atom = Atom(top.getListName()[i],\
                        top.getListNum()[i],\
                        top.getListAtomtype()[i],\
                        {'x':gro.getListx()[i], 'y':gro.getListy()[i], 'z':gro.getListz()[i]},\
                        top.getListCharge()[i],\
                        top.getListEpsilon()[atomtype],\
                        top.getListSigma()[atomtype],\
                        top.getListNumatom()[i])
            #print atom.getName()
            molecule.addAtom(atom)
            
        #print molecule
              
        return molecule
        
