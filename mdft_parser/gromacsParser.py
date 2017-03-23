from atomMaker import *
from moleculeMaker import *
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
    for i in range(top.number_of_atoms):
        atom = Atom(top.list_name[i],\
                    top.list_num[i],\
                    top.list_atomtype[i],\
                    {'x':gro.list_x[i], 'y':gro.list_y[i], 'z':gro.list_z[i]},\
                    top.list_charge[i],\
                    top.list_epsilon[list_atomtype[i]],\
                    top.list_sigma[list_atomtype[i]],\
                    top.list_numatom[i])
        molecule.addAtom(atom)

    molecule.setExpDg(fjson.getCalcDg)
    molecule.setCalcDg(fjson.getExpDg) 
    molecule.setName(fjson.getSystName)
    print molecule.name
          
    return molecule
        
