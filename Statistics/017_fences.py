# %%
"""Return the lower and upper fences of a variable."""

import pandas as pd
from scipy import stats as st
import statsmodels.api as sm

# ======================================================================
# Get things ready
# ======================================================================

X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# ======================================================================
# Return the lower and upper fences
# ======================================================================

pd.Series(
    data={
        "lower": X.quantile(0.25) - 1.5 * st.iqr(X),
        "upper": X.quantile(0.75) + 1.5 * st.iqr(X),
    },
    name="fence",
)
