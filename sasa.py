
import argparse
import subprocess
import os
import numpy as np
import pandas as pd
from pymol import cmd

def hsa(input_pdb,cluster_file,relative):
    cmd.reinitialize()
    cmd.load(input_pdb,'complex')
    cmd.load(cluster_file,'waters')
    numwat=cmd.count_atoms('waters')
    cmd.flag(25,'None')
    if relative==1:
        for i in range(0,numwat):
            cmd.select('resn wat and id '+str(i))
            cmd.copy_to('complex','sele')
            for key,value in cmd.get_sasa_relative('resn wat in complex').items():
                sasa=value
            cmd.remove('resn wat in complex')
            cmd.alter('sele','b='+str(sasa))
        cmd.save('sasa_relative.pdb','waters')
    else:
        for i in range(0,numwat):
            cmd.select('resn wat and id '+str(i))
            cmd.copy_to('complex','sele')
            cmd.set('dot_solvent',1)
            sasa=cmd.get_area('resn wat in complex')
            cmd.remove('resn wat in complex')
            cmd.alter('sele','b='+str(sasa))
        cmd.save('sasa.pdb','waters')
        
def main():
    parser= argparse.ArgumentParser(description='SASA Calculation of waters. SASA value will be loaded into b-factor column of output water PDB file')
    parser.add_argument('-i','--input_pdb',help='Input complex PDB file', required=True)
    parser.add_argument('-c','--cluster_file',help='Input PDB file of waters to analyse',required=True)
    parser.add_argument('-r','--relative',help='Indicate 0 for absolute SASA or 1 for relative SASA',required=True)
    args = parser.parse_args()
    hsa(**vars(args))

if __name__=="__main__":
    main()
    
