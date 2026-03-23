import sys
import numpy as np
import prody
from prody import *

#ANM: 3D model - predicts both magnitude and direction (3D vector for each residue)

def main():
    if len(sys.argv) != 2:
        print("Usage: python anm-fluctuations.py <PDB_ID>")
        sys.exit(1)

    pdb_id = sys.argv[1].lower()
    prody.LOGGER._setverbosity('none')
    structure = parsePDB(pdb_id, subset='ca')

    #Performs Anisotropic Network Model (ANM)
    anm, atoms = calcANM(structure)
    fluctuations = calcSqFlucts(anm[:])
    print(f"Max ANM SqFluct: {np.max(fluctuations):.3f}")

if __name__ == "__main__":
    main()