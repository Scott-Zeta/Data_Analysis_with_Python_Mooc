#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df_UK40 = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    df_Bands = pd.read_csv("src/bands.tsv",sep="\t")
    df_Bands["Band"] = df_Bands["Band"].str.upper()
    df_Bands.loc[:,["Band"]] = df_Bands.loc[:,["Band"]].apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    result = pd.merge(df_UK40,df_Bands,left_on=["Artist"],right_on=["Band"])
    return result

def main():
    result = top_bands()
    print(result)
    return

if __name__ == "__main__":
    main()
