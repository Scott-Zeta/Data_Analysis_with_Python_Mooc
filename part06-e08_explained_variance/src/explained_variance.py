#!/usr/bin/env python3

from sklearn.decomposition import PCA
import pandas as pd
import matplotlib as plt

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep = '\t')
    variance = df.var()
    print(variance)
    pcaModel = PCA()
    pcaModel.fit(df)
    ex_variance = pcaModel.explained_variance_
    print(ex_variance)
    return variance, ex_variance

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))

if __name__ == "__main__":
    main()
