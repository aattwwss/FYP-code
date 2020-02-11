import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

df = pd.read_csv("2012_2017.csv", index_col=0)
df.index = pd.to_datetime(df.index)
"""
for i in range(2013,2018):
    for j in range(1,13):
        df[str(i) + '-'+str(j)].plot()
        #plt.show()
        filename = str(i) + "_" + str(j) + ".png"
        plt.savefig(filename)"""

df["2015-8-1":"2015-8-10"].plot()
plt.show()



