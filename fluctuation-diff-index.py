import sys
import numpy as np
import prody
from prody import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python fluctuation-diff-index.py <PDB_ID>")
        sys.exit(1)

    pdb_id = sys.argv[1].lower()
    prody.LOGGER._setverbosity('none')
    structure = parsePDB(pdb_id, subset='ca')
    gnm, atoms_gnm = calcGNM(structure)
    gnm_fluct = calcSqFlucts(gnm[:])
    anm, atoms_anm = calcANM(structure)
    anm_fluct = calcSqFlucts(anm[:])
    gnm_norm = gnm_fluct / np.max(gnm_fluct)
    anm_norm = anm_fluct / np.max(anm_fluct)
    abs_diff = np.abs(gnm_norm - anm_norm)
    residues = structure.getResnames()
    resnums = structure.getResnums()
    sorted_indices = np.argsort(abs_diff)[::-1]
    
    for i in range(10):
        idx = sorted_indices[i]
        print(f"{abs_diff[idx]:.3f} {idx} {residues[idx]}{resnums[idx]}")

if __name__ == "__main__":
    main()
