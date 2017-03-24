from atom import *
from molecule import *
from parserTop import *
from parserGro import *
from parserJson import *


class GromacsParser:
    def __init__(self, grofile = '', topfile = '', jsonfile = ''):
        self.grofile = grofile
        self.topfile = topfile
        self.jsonfile = jsonfile


    def parse(self):
        gro = ParserGro()
        top = ParserTop()
        fjson = ParserJson()
        
        gro.parseCoord(self.grofile)
        top.parseAtoms(self.topfile)
        fjson.parseEnergies(self.jsonfile, self.grofile[self.grofile.find('/')+1:-4])
        
        molecule = Molecule()
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

        molecule.setExpDg(fjson.getCalcDg() )
        molecule.setCalcDg(fjson.getExpDg() ) 
        molecule.setName(fjson.getSystName() )
        #print molecule.name
              
        return molecule
        
