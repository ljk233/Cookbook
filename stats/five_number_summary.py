# %%
import pandas as pd
from scipy.stats import binom


def five_number_summary(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Return the five-number summary of some data."""
    return df[[col]].describe().T[["min", "25%", "50%", "75%", "max"]]


# Example
# =======
pd.DataFrame({"x": binom(20, 0.6).rvs(100)}).pipe(five_number_summary, "x")

# %%
