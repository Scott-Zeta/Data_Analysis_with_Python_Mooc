#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv",index_col="Region 2018",sep="\t")
    df = df["Akaa":"Äänekoski"]
    df = df[(df["Share of Swedish-speakers of the population, %"] > 5) & (df["Share of foreign citizens of the population, %"] > 5)]
    df = df[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    print(df)
    return df

def main():
    swedish_and_foreigners()

if __name__ == "__main__":
    main()
