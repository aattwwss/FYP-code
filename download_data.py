import pandas as pd
import matplotlib.pyplot as plt
import pytz
import seaborn as sns

start_Date = "201210300700"
end_Date = "201711291800"

def dl_data(start_Date,end_Date):

    df=pd.read_json("https://hourlypricing.comed.com/api?type=5minutefeed&datestart={}&dateend={}".format(start_Date,end_Date))
    df['millisUTC'] = pd.to_datetime(df['millisUTC'], unit='ms',)
    df['millisUTC'] = df['millisUTC'].dt.tz_localize('UTC').dt.tz_convert('US/Central') #convert to US central time, which is where the data is from
    df['millisUTC'] = pd.to_datetime(df['millisUTC'])
    df['millisUTC'] = df['millisUTC'].dt.tz_localize(None) #remove timezone data from column
    df = df.set_index('millisUTC') #set datetime as index of dataframe
    return df


def main():

    df = dl_data(start_Date,end_Date)
    df = df[::-1]

    df.to_csv("2012_2017.csv")

if __name__ == "__main__":
    main()




