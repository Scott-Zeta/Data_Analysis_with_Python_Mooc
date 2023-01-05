#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df.drop(['year','sex','age'],axis = 1,inplace=True)
    df['rate'] = df['suicides_no'] / df['population']
    group = df.groupby('country')
    print(group.get_group("United States of America"))
    result = group['rate'].mean()
    return result

def main():
    print(suicide_fractions())
    return

if __name__ == "__main__":
    main()
