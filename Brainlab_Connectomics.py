
# %%
# Colab installs
import sys
if "google.colab" in sys.modules:
    !pip -q install bctpy statsmodels seaborn

import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu, spearmanr
import seaborn as sns
import bct
from statsmodels.stats.multitest import multipletests

np.random.seed(42)
plt.rcParams.update({"font.size": 14})
