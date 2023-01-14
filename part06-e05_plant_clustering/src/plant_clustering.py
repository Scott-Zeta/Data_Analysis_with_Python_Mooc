#!/usr/bin/env python3

import scipy
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris = load_iris()
    X,y = iris.data, iris.target
    model = KMeans(n_clusters=3,random_state=0)
    model.fit(X)
    permutation = find_permutation(3,y,model.labels_)
    new_cluster = [permutation[l] for l in model.labels_]
    acurt = accuracy_score(y,new_cluster)
    return acurt

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
