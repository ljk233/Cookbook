# %%
"""Select the outliers of a variable using the lower and upper fences method."""

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

lower_fence = X.quantile(0.25) - 1.5 * st.iqr(X)
upper_fence = X.quantile(0.75) + 1.5 * st.iqr(X)
X.to_frame().assign(
    is_inlier=lambda x: x["wage"].between(lower_fence, upper_fence)
).query("not is_inlier")["wage"].rename("outliers (fence)")
