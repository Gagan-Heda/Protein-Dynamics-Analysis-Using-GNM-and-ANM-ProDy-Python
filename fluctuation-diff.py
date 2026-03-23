import sys
import numpy as np
import prody
from prody import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python fluctuation-diff.py <PDB_ID>")
        sys.exit(1)

    pdb_id = sys.argv[1].lower()
    prody.LOGGER._setverbosity('none')
    structure = parsePDB(pdb_id, subset='ca')
    gnm, atoms_gnm = calcGNM(structure)
    gnm_fluct = calcSqFlucts(gnm[:])
    anm, atoms_anm = calcANM(structure)
    anm_fluct = calcSqFlucts(anm[:])
    abs_diff = np.abs(gnm_fluct - anm_fluct)
    max_diff = np.max(abs_diff)
    print(f"Max Abs Difference: {max_diff:.3f}")
    gnm_norm = gnm_fluct / np.max(gnm_fluct)
    anm_norm = anm_fluct / np.max(anm_fluct)
    abs_norm_diff = np.abs(gnm_norm - anm_norm)
    max_norm_diff = np.max(abs_norm_diff)
    print(f"Max Abs Norm Difference: {max_norm_diff:.3f}")

if __name__ == "__main__":
    main()
