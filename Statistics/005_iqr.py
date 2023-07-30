# %%
"""Return the interquartile-range of a dataset."""

import pandas as pd
from scipy import stats as st
import statsmodels.api as sm

# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# ======================================================================
# Return the IQR
# ======================================================================

st.iqr(X)
