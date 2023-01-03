"""
This script is targeted to clean smiles, aiming to include molecules with C, H, O only

"""
import numpy as np
from openchem.data.utils import read_smiles_property_file

data = read_smiles_property_file('./datasets/molecules_raw.smi',
                                 cols_to_read=[0,1],
                                 keep_header=False)

smiles=np.array(data[0])

def check_cho(smile):
    chars_to_check = ['N','F','Be','B','F','Si','P','S','Cl','As','Se','Br','I','Li','s','n',\
                      'Na','Mg','Al','K','Ca','Sc','Ti','V','Cr','Mn', 'Fe','Co','Ni','Cu',\
                      'Zn','Ga','Ge','As','Se','Br','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru',\
                      'Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Cs','Ba','Hf','Ta',\
                      'W','Re','Os','Ir','Pt','Au','Hg','TI','Pb','Bi','Po','At','Rn',]
    for char in chars_to_check:
        if char in smile:
            l=1
            break
        else:
            l=0
    if l==1:
        return False
    else:
        return True

def clean_smiles(smiles):
   bool_array=np.array(list(map(check_cho,smiles))) 
   cleaned_smiles=smiles[np.argwhere(bool_array==True)]
   return cleaned_smiles

def save_smiles(path, smiles):
    f = open(path, 'w')
    n_targets = smiles.shape[1]
    for i in range(len(smiles)):
        f.writelines(smiles[i])
        f.writelines('\n')
    f.close()

cleaned=clean_smiles(smiles)
save_smiles('./datasets/molecules_cleaned',cleaned)


