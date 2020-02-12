import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

# Import data
df = pd.read_csv('data/1000.csv', names=['value'], header=0, index_col=0)

# Original Series
#fig, axes = plt.subplots(3, 2, sharex=True)
#axes[0, 0].plot(df.value); axes[0, 0].set_title('Original Series')
plot_pacf(df.value,lags=50)

plt.show()