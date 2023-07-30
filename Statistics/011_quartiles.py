# %%
"""Return the quartiles of a dataset."""

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

X.quantile(np.linspace(0.25, 1, num=4)).rename("quartiles")
