import pandas as pd
from sklearn import preprocessing

def normalised(df,col):

    # Create x, where x the 'scores' column's values as floats
    x = df[[col]].values.astype(float)

    # Create a minimum and maximum processor object
    min_max_scaler = preprocessing.MinMaxScaler()

    # Create an object to transform the data to fit minmax processor
    x_scaled = min_max_scaler.fit_transform(x)

    # Run the normalizer on the dataframe
    df_normalized = pd.DataFrame(x_scaled)
    return df_normalized