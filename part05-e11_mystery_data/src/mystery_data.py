#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv",sep="\t")
    model = LinearRegression(fit_intercept=False)
    x = df.iloc[:,0:5]
    y = df.iloc[:,5]
    # print(x)
    # print(y)
    model.fit(x,y)
    print(df.head())
    return [x for x in model.coef_]

def main():
    coefficients = mystery_data()
    print(coefficients)
    # print the coefficients here
    
if __name__ == "__main__":
    main()
