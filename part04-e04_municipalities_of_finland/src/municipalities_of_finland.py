#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv",sep="\t",index_col="Region 2018")
    result = df["Akaa":"Äänekoski"]
    print(result.head())
    return result

def main():
    municipalities_of_finland()
    return
    
if __name__ == "__main__":
    main()
