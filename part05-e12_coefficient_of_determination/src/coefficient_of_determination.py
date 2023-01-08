#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv",sep="\t")
    model = linear_model.LinearRegression(fit_intercept=True)
    x = df.iloc[:,0:5]
    y = df.iloc[:,5]
    model.fit(x,y)
    R2 = []
    R2.append(model.score(x,y))
    for column in x:
        sub_X = df.loc[:,column]
        sub_X = sub_X.values.reshape(-1,1)
        model.fit(sub_X,y)
        R2.append(model.score(sub_X,y))
    return R2
    
def main():
    R2 = coefficient_of_determination()
    print(R2)
    return

if __name__ == "__main__":
    main()
