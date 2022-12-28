#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df.drop(df[(df['LW'] == "New") | (df['LW'] == "Re")].index, inplace=True)
    df["WoC"] -= 1
    df["LW"] = df["LW"].astype(int)
    # reach the peak on this week, since can not confirm history position, subsitute with NA
    # for position, smaller the better, fucking df['Pos'] < df['Lw'] means its increase this week
    df.loc[(df['Peak Pos'] == df["Pos"]) & (df['Pos'] < df['LW']), 'Peak Pos'] = np.nan
    df = df.sort_values(by=['LW'])
    df.index = df["LW"]
    df = df.reindex(range(1,41)) # fill NA with missing row
    df["Pos"] = df.index
    df["LW"] = np.nan
    print(df)
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
