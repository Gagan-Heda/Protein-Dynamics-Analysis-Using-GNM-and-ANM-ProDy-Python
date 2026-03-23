# Protein Dynamics Analysis Using GNM and ANM (ProDy + Python)

Python-based pipeline for analyzing protein structural dynamics using elastic network models. Implements Gaussian Network Model (GNM) and Anisotropic Network Model (ANM) to compute residue-level fluctuations, compare modeling approaches, and identify structurally significant regions.

---

## Overview

Protein motions are fundamental to biological function. This project models intrinsic fluctuations in protein structures using two complementary elastic network approaches:

- **GNM (Gaussian Network Model)** – isotropic fluctuations based on residue connectivity  
- **ANM (Anisotropic Network Model)** – directional fluctuations capturing collective motions  

The workflow highlights dynamic differences and identifies key residues contributing to structural flexibility.

---

## Objectives

- Compute residue-level fluctuations using GNM and ANM  
- Compare fluctuation magnitudes between models  
- Normalize and quantify differences for fair comparison  
- Identify residues with the largest dynamic discrepancies  

---

## Scripts

- `gnm-fluctuations.py`  
  - Calculates GNM-based squared fluctuations for Cα atoms  

- `anm-fluctuations.py`  
  - Calculates ANM-based squared fluctuations  

- `fluctuation-diff.py`  
  - Computes absolute and normalized differences between GNM and ANM  

- `fluctuation-diff-index.py`  
  - Extracts residues with the highest normalized fluctuation differences  

---

## Methodology

### Elastic Network Modeling
- **GNM:** connectivity-based, isotropic fluctuations  
- **ANM:** includes directional interactions, captures anisotropic motions  

### Fluctuation Analysis
- Based on normal mode analysis  
- Computed for all Cα atoms  
- Uses full spectrum of modes for accurate modeling  

### Normalization
- Maximum fluctuation scaled to 1 for each model  
- Allows direct comparison across GNM and ANM  

### Residue Mapping
- Maps results to:
  - Residue index  
  - Residue name and number  

---

## Technologies

- Python  
- ProDy  
- NumPy  

---

## Key Features

- Automated PDB structure retrieval  
- Comparative fluctuation modeling (GNM vs ANM)  
- Residue-level analysis of protein dynamics  
- Normalized comparison of fluctuations  
- Identification of residues critical for structural flexibility  

---

## Skills Demonstrated

- Structural bioinformatics and protein dynamics  
- Elastic network modeling (GNM/ANM)  
- Normal mode analysis  
- Scientific computing in Python  
- Data normalization and comparative analysis  
- Interpretation of structure–function relationships  

---

## Notes

- Fluctuation calculations are limited to Cα atoms  
- Differences between models stem from isotropic vs anisotropic assumptions  
- Output values reported to three decimal places  

---

## Author

**Gagan Heda**
