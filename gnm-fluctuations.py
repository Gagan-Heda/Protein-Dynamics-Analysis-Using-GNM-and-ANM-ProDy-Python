import sys
import numpy as np
import prody
from prody import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python gnm-fluctuations.py <PDB_ID>")
        sys.exit(1)

    pdb_id = sys.argv[1].lower()
    prody.LOGGER._setverbosity('none')
    structure = parsePDB(pdb_id, subset='ca')
    gnm, atoms = calcGNM(structure)

    #Returns a 1D numpy array where each element is the 
    # squared fluctuation for one C-alpha atom
    fluctuations = calcSqFlucts(gnm[:])
    print(f"Max GNM SqFluct: {np.max(fluctuations):.3f}")

if __name__ == "__main__":
    main()