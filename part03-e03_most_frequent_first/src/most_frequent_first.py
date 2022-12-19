#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    unique,inverse,counts = np.unique(a[:,c],return_inverse = True,return_counts=True)
    print(unique)
    print(inverse)
    print(counts)

    # This array indicates the count of each element in the original array a[:,c]. 
    # For example, the first element of the original array is 1, which appears twice in the original array, 
    # so the first element of the resulting array is 2. The second element of the original array is 2, 
    # which appears three times in the original array, so the second element of the resulting array is 3, and so on.
    # CORE
    print(counts[inverse])
    # hash the counts on inverse (actually rebuild the inverse with counts elements)
    idx = np.flip(np.argsort(counts[inverse]))
    print(idx)
    return a[idx]

def main():
    np.random.seed(1)
    a = np.random.randint(0,9,size=(8,8))
    print(a)
    print(most_frequent_first(a,-1))

if __name__ == "__main__":
    main()
