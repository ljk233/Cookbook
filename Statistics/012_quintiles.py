# %%
"""Return the quintiles of a dataset."""

import numpy as np
import pandas as pd
import statsmodels.api as sm

# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# ======================================================================
# Return the Nth percentile
# ======================================================================

X.quantile(np.linspace(0.2, 1, num=5)).rename("quintiles")
