#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1,index= ["a","b","c"])
    s2 = pd.Series(L2,index= ["a","b","c"])
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    s2 = s2.drop(['b'])
    return (s1, s2)
    
def main():
    L1 = [1,2,3]
    L2 = [4,5,6]
    s1,s2 = create_series(L1,L2)
    s1,s2 = modify_series(s1,s2)
    print(s1)
    print(s2)
    print(s1+s2)
    print(s1.add(s2))
    
if __name__ == "__main__":
    main()
