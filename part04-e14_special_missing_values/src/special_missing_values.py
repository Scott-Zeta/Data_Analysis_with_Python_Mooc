#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df.replace({"New": np.nan, "Re": np.nan},inplace=True)
    df["LW"] = df["LW"].astype(float)
    mask = df["Pos"] > df["LW"]
    seleted = df[mask]
    print(seleted)
    print(seleted.shape)
    return seleted

# double mask method from model solution
def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    m = (df["LW"] == "New") | (df["LW"] == "Re")
    df.loc[m, "LW"] = np.nan
    df["LW"] = pd.to_numeric(df["LW"])
    m2 = df["LW"] < df["Pos"]
    return df[m2]

def main():
    special_missing_values()

if __name__ == "__main__":
    main()
