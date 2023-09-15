
# Pooled sample variance

## Notes

*[Confidence Interval for Two Independent Samples, Continuous Outcome](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/BS704_Confidence_Intervals5.html#headingtaglink_1)* (Boston University School of Public Health, 2017)

> If we assume equal variances between groups, we can pool the information on variability (sample variances) to generate an estimate of the population variability.
> Therefore, the standard error (SE) of the difference in sample means is the pooled estimate of the common standard deviation *S*<sub>*P*</sub> (assuming that the variances in the populations are similar) computed as the weighted average of the standard deviations in the samples[.]

## Example

Import the dependencies.

```python
import pandas as pd
```

Load the data.

```python
skull = pd.read_parquet("../data/skull.parquet")
```

Return the pooled sample variance and standard deviation of the breadth of Etruscan and modern Italian skulls.

*Note, we use use generic variable names, so the recipe does not have to be altered.*

```python
# Collect the samples
samp1 = skull.query("skull == 'etruscan'")["breadth"]
samp2 = skull.query("skull == 'italian'")["breadth"]

# Declare and initialise parameters of interest
n1, v1 = samp1.shape[0], samp1.var()
n2, v2 = samp2.shape[0], samp2.var()

# Output the pooled var, pooled std
pooled_var = (v1 * (n1 - 1) + v2 * (n2 - 1)) / (n1 + n2 - 2)
pooled_var, pooled_var ** 0.5
```
