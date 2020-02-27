import pandas as pd 
import matplotlib.pyplot as plt

df1 = pd.read_csv("WEP/WEP_Combined-2019.csv")
df2 = pd.read_csv("MG/MG_Combined-2019.csv")
df3 = pd.read_csv("USEP/USEP_Combined-2019.csv")

ax = plt.gca()

df1.plot(kind='line',x='DATE',y='WEP ($/MWh)', ax=ax)

#df2.plot(kind='line',x='DATE',y='USEP ($/MWh)', color='red', ax=ax)

df3.plot(kind='line',x='DATE',y='USEP ($/MWh)', color='red', ax=ax)

df1['WEP ($/MWh)'].corrwith(df3['USEP ($/MWh)']) 

#plt.show()