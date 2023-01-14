#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

# function for label permutation
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    # read dataframe
    df = pd.read_csv("src/data.tsv",sep="\t")
    X = df.iloc[:,0:2]
    y = df.iloc[:,2]
    for n in np.arange(0.05,0.2,0.05):
        model = DBSCAN(eps=n)
        model.fit(X)
        # -1 in cluster label means the noisy point
        n_cluster = len(np.unique(model.labels_)) - (1 if -1 in model.labels_ else 0)
        if n_cluster == len(np.unique(y)):
            permutation = find_permutation(n_cluster,y,model.labels_)
            new_labels = [permutation[label] for label in model.labels_]
            acc = accuracy_score(y,new_labels)
        else:
            acc = np.nan
        print(f'{n}:{acc}')

    return pd.DataFrame()

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
