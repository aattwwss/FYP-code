Import the libraries
```
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
from scipy import stats
from sklearn import preprocessing

```

Load in dataset
```
df = pd.read_csv("2019_full_data.csv", index_col=0, parse_dates=True)

df = pd.read_csv("2015_2019_WEP_TS.csv", index_col=0, parse_dates=True)
```

Imputing using linear interpolation

```
df = df.assign(InterpolateSLinear=df.price.interpolate(method='slinear'))
```

Plot specific month/day

```
df["2019-04"]["WEP ($/MWh)"].plot(style="-")
```

Seasonality
```
fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
for name, ax in zip(['WEP'], axes):
    sns.boxplot(data=df, x='Month', y=name, ax=ax)
ax.set_ylabel('Price')
ax.set_title(name)
# Remove the automatic x-axis label from all but the bottom subplot
if ax != axes[-1]:
    ax.set_xlabel('')

```