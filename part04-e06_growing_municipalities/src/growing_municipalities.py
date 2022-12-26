#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    riseDf = df[df["Population change from the previous year, %"]> 0]
    print(riseDf)
    return len(riseDf)/len(df)

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    df = df["Akaa":"Äänekoski"]
    rate = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {rate:.1f}%") #should not have "%" in here

if __name__ == "__main__":
    main()
