from atom import *
from molecule import *

class MdftDBParser:
    "This class defines a parser for our MDFT database in JSON format"
    def __init__(self, mdft_mol = ''):
        self.mdft_mol = mdft_mol
        
    def parse(self, json_db, mol_name):
        with open(json_db, 'r') as json_file :
            mdft_db = json.load(json_file)
        
        with open('mdft_atomtypes.json', 'r') as json_atypes:
            dict_atypes = json.load(json_atypes)
        
        molecule = Molecule()
        for at in mdft_db[mol_name]:
            atome = Atome(at['name'],\
                          at['index'],
                          at['atomtype'],\
                          {'x':at['x'], 'y':at['y'], 'z':at['z']},\
                          at['charge'],\
                          dict_atypes[at['atomtype']]['epsilon'],\
                          dict_atypes[at['atomtype']]['sigma'],\
                          at['Zatomic'])
            molecule.addAtom(atome)
        
        return molecule
                        
            
