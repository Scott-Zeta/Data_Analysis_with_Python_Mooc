#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")
    print(df)
    result = df.groupby('Publisher')['WoC'].sum().sort_values(ascending=False)
    mask = result.index[0]
    return df[df['Publisher'] == mask]

def main():
    print(best_record_company())
    return
    

if __name__ == "__main__":
    main()
