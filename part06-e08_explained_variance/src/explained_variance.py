#!/usr/bin/env python3

from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep = '\t')
    variance = df.var()
    # print(variance)
    pcaModel = PCA()
    pcaModel.fit(df)
    ex_variance = pcaModel.explained_variance_
    # print(ex_variance)
    return variance, ex_variance

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    vlist = " ".join(f'{x:.3f}' for x in v)
    evlist = " ".join(f'{x:.3f}' for x in ev)
    print(f"The variances are: {vlist}")
    print(f"The explained variances after PCA are: {evlist}")
    plt.plot(np.arange(1,11), np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()
