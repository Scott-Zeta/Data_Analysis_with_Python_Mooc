#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def toint(x):
    dic = {"A":0,"C":1,"G":2,"T":3}
    return dic[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename,sep="\t")
    X = df["X"]
    y = df["y"]
    y = y.to_numpy()
    X = X.to_numpy()
    new_X = []
    for s in X:
        new_element = []
        for char in s:
            new_element.append(toint(char))
        new_X.append(np.array(new_element))
    X = np.array(new_X)
    print(X)
    return (X, y)

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    return 0.0

def cluster_hamming(filename):
    return 0.0


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))
    print(get_features_and_labels("src/data.seq"))
if __name__ == "__main__":
    main()
