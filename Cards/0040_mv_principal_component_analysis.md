
# Principal component analysis

*2023-09-21*

A cheat sheet for performing dimension reduction using principal component analysis.

## Main

Import the dependencies.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn import datasets
import seaborn as sns
from matplotlib import pyplot as plt
```

Set the graphing theme.

```python
sns.set_theme()
```

Load the data.

```python
X, _ = datasets.load_iris(return_X_y=True, as_frame=True)
```

### Prepare the data

Replace numerical targets with labels.

<!-- #raw -->
y_ = y.map(lambda d: {0: "setosa", 1: "versicolor", 2: "virginica"}[d])
<!-- #endraw -->

Split the data into test and train.

<!-- #raw -->
X_train, X_test, y_train, y_test = train_test_split(
    X, y_, test_size=0.15, random_state=21
)
<!-- #endraw -->

Merge *X_train*, *y_train* for exploratory data analysis.

<!-- #raw -->
iris_train = X_train.assign(target=y_train)
<!-- #endraw -->

### Exploratory data analysis

Describe the data.

```python
X.describe().T
```

Plot a scatterplot matrix.

```python
X.pipe(sns.pairplot, corner=True)
```

Plot a correlation heatmap.

```python
X.corr().pipe(sns.heatmap, vmin=-1, center=0, cmap="bwr", square=True)
```

Plot a profile plot of each target.
In a profile plot,

> [...] each variable in the multivariate data set is represented by a category along the *x*-axis.
> The values for each of the variables are then plotted along the *y*-axis.
> Finally, the points corresponding to the same observation are joined by a line.

```python
X.melt().pipe(sns.relplot, x="variable", y="value", kind="line", errorbar="sd")
plt.title("Profile plot")
```

### Train the model

Standardise the data.

```python
standard_scaler = StandardScaler()
Z = standard_scaler.fit_transform(X)
```

Model and fit the data.

```python
pca_model = PCA()
result = pca_model.fit_transform(Z)
```

Return the variance explained by each principal component.

```python
pd.DataFrame(
    data={
        "VE": pca_model.explained_variance_,
        "PVE": pca_model.explained_variance_ratio_ * 100
    },
    index=pd.RangeIndex(1, 5, name="PC")
).assign(CPVE=lambda x: x['PVE'].cumsum())
```

Return the loadings.

```python
pd.DataFrame(
    pca_model.components_,
    columns=X.columns,
    index=pd.RangeIndex(1, 5, name="PC")
)
```

Plot a scree plot of the principal component against total variance explained.

```python
plt.plot(range(1, 5), pca_model.explained_variance_, "o-")
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
```
