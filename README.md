# IST Winter School 2026 - Connectomics Lab

This repository contains material for the **Connectomics
Hands-On**.\
The lab introduces basic **network neuroscience / connectomics**
concepts using graph-theoretic measures.

The notebook is designed to run entirely in **Google Colab**, so
students do **not need to install Python** locally.\
However, section "**Running locally (optional)**" below provides instructions
to run the lab on a local machine.

------------------------------------------------------------------------

## Open the lab in Google Colab

Click the badge below:

[![Open In
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agriffa/IST_Connectomics_Lab/blob/main/IST_Connectomics_Lab_colab.ipynb)

When the notebook opens:

1.  Click **File → Save a copy in Drive**
2.  Close GitHub 'IST_Connectomics_Lab_colab.ipynb' 
3.  Work through the exercises.

------------------------------------------------------------------------

## Learning objectives

During this lab you will learn how to:

-   Inspect structural connectivity matrices
-   Build binary graphs from weighted networks
-   Compute network density and degree
-   Build a consensus connectome
-   Compute graph measures:
    -   global efficiency
    -   clustering coefficient
    -   characteristic path length
    -   small-world index
-   Compare connectomes between two groups (CTRL vs SCHZ)
-   Perform statistical testing and FDR correction
-   Visualize your connectome and nodal properties

------------------------------------------------------------------------

## Repository structure

    connectomics-lab/
    │
    ├── connectomics_lab_colab.ipynb
    ├── Data/
    │   ├── Brainlab_Connectomics_Data.npz
    │   ├── Brainlab_Connectomics_Labels.json
    │   └── Euclidean_Distance.npz
    │   └── Original_Connectomics_Data.npz

------------------------------------------------------------------------

## Data files

  ---------------------------------------------------------------------------
  File                                    Description
  --------------------------------------- -----------------------------------
  **Brainlab_Connectomics_Data.npz**      Structural connectivity matrices
                                          (CTRL and SCHZ)

  **Brainlab_Connectomics_Labels.json**   Brain region labels

  **Euclidean_Distance.npz**              Euclidean distance between region
                                          centroids
  ---------------------------------------------------------------------------

All files are automatically downloaded when the notebook starts.

------------------------------------------------------------------------

## Required Python libraries

The notebook installs the required packages automatically in Colab:

-   numpy
-   matplotlib
-   bctpy (Brain Connectivity Toolbox for Python)
-   seaborn
-   statsmodels

No manual installation is needed.

------------------------------------------------------------------------

## Running locally (optional)

1.  Downalod the Connectomics Lab material from GitHub
    [IST_Connectomics_Lab](https://github.com/agriffa/IST_Connectomics_Lab/tree/main)
    and unzip the folder.
2.  Check whether conda is available on your machine by typing
    ```
    conda info
    ```
    If conda is not available on your machine, [install miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install).
3.  Create a conda environment for this lab, activate the environment,
    *pip* install the required Python libraries, and start JupyterLab:
    
    ```
    conda create -n brainlab_env python=3.11
    conda activate brainlab_env
    pip install numpy matplotlib bctpy seaborn statsmodels jupyter ipykernel
    python -m ipykernel install --user --name brainlab_env
    jupyter lab
    ```
4.  Open *IST_Connectomics_Lab_colab.ipynb* in JupyterLab.
    Select 'brainlab_env' kernel using the menu on the top right corner.  

**IMPORTANT** start JupyterLab from inside the repository folder:
```
cd IST_Connectomics_Lab-main
jupyter lab
```

------------------------------------------------------------------------

## License

-   Code: MIT License
-   Data: CC BY 4.0 (see *DATA_LICENSE.md*)
