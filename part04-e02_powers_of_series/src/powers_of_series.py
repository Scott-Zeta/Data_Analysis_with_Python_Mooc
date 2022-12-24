#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    result = pd.DataFrame()
    for n in range(1,k+1):
        col = pd.Series(s**n, name = n)
        print(col)
        result = pd.concat([result,col],axis=1)
    return result

# dictionary method
def powers_of_series(s, k):
    c=[ s**i for i in range(1,k+1) ]
    df = pd.DataFrame(dict(zip(range(1,k+1), c)))
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()