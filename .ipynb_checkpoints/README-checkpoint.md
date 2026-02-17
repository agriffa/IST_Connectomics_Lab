# IST Winter School 2026 - Connectomics Lab (Python + Colab)

This repository contains material for the **Connectomics
Hands-On**.\
The lab introduces basic **network neuroscience / connectomics**
concepts using graph-theoretic measures.

The notebook is designed to run entirely in **Google Colab**, so
students do **not need to install Python** locally.

------------------------------------------------------------------------

## Open the lab in Google Colab

Click the badge below:

[![Open In
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agriffa/IST_Connectomics_Lab/blob/main/connectomics_lab_colab.ipynb)

When the notebook opens:

1.  Click **File → Save a copy in Drive**
2.  Click **Runtime → Run all**
3.  Work through the exercises.

------------------------------------------------------------------------

## Learning objectives

During this lab you will learn how to:

-   Inspect structural connectivity matrices
-   Build binary graphs from weighted networks
-   Compute network density and degree
-   Build a **consensus connectome**
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
    │   └── Edist.npy

------------------------------------------------------------------------

## Data files

  ---------------------------------------------------------------------------
  File                                    Description
  --------------------------------------- -----------------------------------
  **Brainlab_Connectomics_Data.npz**      Structural connectivity matrices
                                          (CTRL and SCHZ)

  **Brainlab_Connectomics_Labels.json**   Brain region labels
  
  **Edist.npy**                           Euclidean distance between region
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

    conda create -n connectomicslab python=3.11
    conda activate connectomicslab
    pip install numpy matplotlib bctpy seaborn statsmodels jupyter
    jupyter lab

Then open `IST_Connectomics_Lab_colab.ipynb`.

------------------------------------------------------------------------

## License

-   Code: MIT License\
-   Data: CC BY 4.0
