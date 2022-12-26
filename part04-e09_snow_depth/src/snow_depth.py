#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    max = df.iloc[:,6].max()
    return max

def main():
    print(f"Max snow depth: {snow_depth()}")

if __name__ == "__main__":
    main()
