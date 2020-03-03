Import the libraries
```
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats
from sklearn import preprocessing
```

Load in dataset
```
df = pd.read_csv("electric_price.csv", index_col=0, parse_dates=True)
```

Imputing using linear interpolation

```
df = df.assign(InterpolateSLinear=df.price.interpolate(method='slinear'))
```

Plot specific month/day

```
df["2019-04"]["WEP ($/MWh)"].plot(style="-")
```

