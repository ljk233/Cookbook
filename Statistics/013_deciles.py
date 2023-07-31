# %%
"""Return the deciles of a dataset."""

import numpy as np
import pandas as pd
import statsmodels.api as sm


# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# ======================================================================
# Return the deciles
# ======================================================================

X.quantile(np.linspace(0.1, 1, num=10)).rename("deciles")
