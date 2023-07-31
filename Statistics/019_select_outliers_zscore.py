# %%
"""Select the outliers of a variable using the zscore method."""

import pandas as pd
from scipy import stats as st
import statsmodels.api as sm

# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# ======================================================================
# Return the deciles
# ======================================================================

X.to_frame().assign(is_inlier=lambda x: st.zscore(x["wage"]).between(-3, 3)).query(
    "not is_inlier"
)["wage"].rename("outliers (zscore)")
