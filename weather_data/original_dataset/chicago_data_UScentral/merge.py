import pandas as pd
import sys

def main():

    file_name = sys.argv[1]
    file_name2 = sys.argv[2]
    df = pd.read_csv(file_name, index_col=0)
    df2 = pd.read_csv(file_name2, index_col=0)
    df3 = pd.merge(df, df2, left_on="datetime", right_on="datetime", how='outer', suffixes=('', '_y'))
    #df3 = df3.drop(list(df3.filter(regex='_y$')), axis=1)

    print (df3.head(1000))
    df3.to_csv("merged.csv", index=False)


if __name__ == "__main__":
    main()