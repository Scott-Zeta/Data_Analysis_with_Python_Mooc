#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    july = df[df["m"] == 7]
    average = july.iloc[:,7].mean()
    print(average)
    return average

def main():
    print(f"Average temperature in July: {average_temperature():.1f}")

if __name__ == "__main__":
    main()
