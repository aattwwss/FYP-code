import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns
from scipy import stats
from sklearn import preprocessing

df_2019 = pd.read_csv("2019_full_data.csv", index_col=0, parse_dates=True)
df_2019_backup = df_2019.copy()

df_WEP = pd.read_csv("2015_2019_WEP_TS.csv", index_col=0, parse_dates=True)
df_WEP_backup = df_WEP.copy() 

#Replace outlier with upper limit
std = df_WEP['WEP'].std()
mean = df_WEP['WEP'].mean()
df_WEP['WEP'].loc[df_WEP['WEP'] > mean + 3*std] = mean + 3*std

#Add time information into data
df_WEP=df_WEP.resample("H").mean()
df_WEP['Year'] = df_WEP.index.year
df_WEP['Month'] = df_WEP.index.month
df_WEP['day_of_week'] = df_WEP.index.day_name()
df_WEP['day_of_week_int'] = df_WEP.index.dayofweek
df_WEP['hour'] = df_WEP.index.hour

df_WEP['2019']['WEP'].plot()
plt.show()