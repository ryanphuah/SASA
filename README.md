# SASA
SASA calculation of waters around ligand in a complex
<details>
<summary><b>Help documentation</b> </summary>

    usage: sasa.py [-h] -i INPUT_PDB -c CLUSTER_FILE -r RELATIVE

    SASA Calculation of waters. SASA value will be loaded into b-factor column of output water PDB file
    
    options:
      -h, --help            show this help message and exit
      -i INPUT_PDB, --input_pdb INPUT_PDB
                            Input complex PDB file
      -c CLUSTER_FILE, --cluster_file CLUSTER_FILE
                            Input PDB file of waters to analyse
      -r RELATIVE, --relative RELATIVE
                            Indicate 0 for absolute SASA or 1 for relative SASA


</details>

## Install Pymol using conda
Pymol can be installed with the following lines of code
```
conda install conda-forge::pymol-open-source
```
## Running SASA Calculations
The following line can be run for the test files provided
```
python sasa.py -i 1ec1_complex_lastframe.pdb -c 1ec1_clustercenterfile.pdb -r 0
```
Do note the -r flag is used to specify type of SASA calculated (absolute vs relative). Relative SASA outputs a value between 0 (fully buried) and 1 (fully exposed). Reference output files are labelled _ref.pdb for both cases.
