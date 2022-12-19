#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    unique,counts = np.unique(a[:,c],return_counts=True)
    idx = np.flip(np.argsort(counts))
    print(unique[idx])
    print(counts[idx])
    a = a[:,unique[idx]]
    return a

def main():
    np.random.seed(1)
    a = np.random.randint(0,9,size=(8,8))
    print(a)
    print(most_frequent_first(a,-1))

if __name__ == "__main__":
    main()
