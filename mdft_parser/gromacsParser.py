from atom import *
from molecule import *
from parserTop import *
from parserGro import *
from parserJson import *


class GromacsParser:
    "This class manages which .gro and .top files to parse and submit them to .gro (parserGro) and .top (parserTop) parsers"
    def __init__(self, mdft_db = None):
        self.mdft_db = mdft_db

    def parse(self, mol):
        #Parse data from given .gro and .top files reformat them to generate atoms, then molecules"
        gro = ParserGro()
        top = ParserTop()
        gro.parseCoord(self.mdft_db+'/'+mol+".gro")
        top.parseAtoms(self.mdft_db+'/'+mol+".top")
        
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
