#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv("src/municipal.tsv", sep="\t",index_col=0)
    result = df.loc["Akaa":"Äänekoski",["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    print(result)
    return result

def main():
    subsetting_with_loc()
    return

if __name__ == "__main__":
    main()
