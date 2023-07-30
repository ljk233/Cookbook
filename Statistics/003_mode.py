# %%
"""Return the mode of a dataset."""

import pandas as pd
import statsmodels.api as sm

# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("SwissLabor", "AER").data["education"]

# ======================================================================
# Return the mode
# ======================================================================

X.value_counts().head(1)
