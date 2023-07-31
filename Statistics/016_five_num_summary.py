# %%
"""Return the five-number summary.

(The function is suitable for piping.)
"""

import pandas as pd
import statsmodels.api as sm

# ======================================================================
# Function
# ======================================================================


def five_num_summary(se: pd.Series) -> pd.Series:
    """Return the five-number summary."""
    return pd.Series(
        data={
            "min": se.min(),
            "lower quartile": se.quantile(0.25),
            "median": se.median(),
            "upper quartile": se.quantile(0.75),
            "max": se.max(),
        },
        name="five-number summary",
    )


# ======================================================================
# Example
# ======================================================================

# Get things ready
X: pd.Series = sm.datasets.get_rdataset("Bwages", "Ecdat").data["wage"]

# Return the five-number summary
X.pipe(five_num_summary)
