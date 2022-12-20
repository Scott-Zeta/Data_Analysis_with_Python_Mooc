#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    dataset = load()
    sepalLength = dataset[:,0]
    petalLength = dataset[:,2]
    r,p = scipy.stats.pearsonr(sepalLength,petalLength)
    return r

def correlations():
    dataset = load()
    sepalLength = dataset[:,0]
    sepalWidth = dataset[:,1]
    petalLength = dataset[:,2]
    petalWidth = dataset[:,3]
    correlations = np.corrcoef([sepalLength,sepalWidth,petalLength,petalWidth])
    return correlations

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
