import pandas as pd 
import sys
import pytz


def main():

    file_name = sys.argv[1]
    df=pd.read_csv(file_name)

    df['datetime'] = pd.to_datetime(df['datetime'])
    df['datetime'] = df['datetime'].dt.tz_localize('UTC').dt.tz_convert('US/Central')
    df['datetime'] = df['datetime'].dt.tz_localize(None)
    df = df.set_index('datetime')

    new_name = "chicago_" + file_name[7:]

    print (df.info())
    print (new_name)

    df.to_csv(new_name)


if __name__ == "__main__":
    main()

