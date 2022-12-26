#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    belowZero = df[df.iloc[:,7] < 0]['Air temperature (degC)'].count()
    return belowZero

def main():
    print(f"Number of days below zero: {below_zero()}")
    
if __name__ == "__main__":
    main()
