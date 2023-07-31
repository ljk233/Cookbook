# %%
"""Return the sample variance of a dataset."""

import pandas as pd
import statsmodels.api as sm

# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# ======================================================================
# Return the sample variance
# ======================================================================

X.var(ddof=1)
