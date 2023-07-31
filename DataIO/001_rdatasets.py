# %%
"""Retrieving data from rdatasets"""

import statsmodels.api as sm

# Cache the data
smoke_ban = sm.datasets.get_rdataset("SmokeBan", "AER", cache=True)

# Access the underlying data. Returns a pd.DataFrame
smoke_ban.data
