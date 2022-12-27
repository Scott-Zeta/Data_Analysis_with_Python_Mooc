#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    print(df.shape)
    result = df.dropna(axis = 1, how="all")
    result = result.dropna(how = "all")
    print(result.shape)
    return result


def main():
    cyclists()
    return
    
if __name__ == "__main__":
    main()
