# %%
"""Return the range of a dataset."""

import numpy as np
import pandas as pd
import statsmodels.api as sm

# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# ======================================================================
# Return the range
# ======================================================================

np.ptp(X)
