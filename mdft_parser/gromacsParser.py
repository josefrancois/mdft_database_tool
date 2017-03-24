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
    fjson.parseEnergies(jsonfile, grofile[grofile.find('/')+1:-4])
    
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
        
