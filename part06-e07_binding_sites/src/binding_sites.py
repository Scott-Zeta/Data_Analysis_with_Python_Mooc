#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

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
    return (X, y)

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    data = get_features_and_labels(filename)
    X = data[0]
    y = data[1]
    # affinity for distance method between point, linkage for distance between cluster
    model = AgglomerativeClustering(n_clusters= 2, affinity= "euclidean", linkage="average")
    model.fit(X)
    permutation = find_permutation(2,y,model.labels_)
    y_fitted = [permutation[label] for label in model.labels_]
    acc = accuracy_score(y,y_fitted)
    return acc

def cluster_hamming(filename):
    data = get_features_and_labels(filename)
    X = data[0]
    y = data[1]
    # this will out put a matrix of distance between each point of X
    distance = pairwise_distances(X, metric='hamming')
    # precomputed means distance already computed, must be a matrix
    model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
    model.fit(distance)
    permutation = find_permutation(2,y,model.labels_)
    y_fitted = [permutation[label] for label in model.labels_]
    acc = accuracy_score(y,y_fitted)
    return acc


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))
    print(get_features_and_labels("src/data.seq"))
if __name__ == "__main__":
    main()
