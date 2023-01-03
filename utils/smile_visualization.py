#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:39:49 2022

@author: cheng
"""
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

# smiles_path='./generated_molecules/sampled_molecules.txt'
# df=pd.read_table(smiles_path,header=None)
# molecules=df.values.tolist()

def save_smiles_graph(smiles):
    mol=Chem.MolFromSmiles(smiles)
    Draw.ShowMol(mol,size=(550,550),kekulize=True)
    #Draw.MolToFile(mol, './generated_molecules/visualization/'+smiles+'.png',size=(250,250))

# for molecule in molecules:
#     save_smiles_graph(str(molecule[0]))

save_smiles_graph('C{-}C{n+}')