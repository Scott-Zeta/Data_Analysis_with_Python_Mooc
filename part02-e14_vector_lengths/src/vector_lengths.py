#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(np.square(a),axis = 1))

def main():
    a = np.array([[5, 1, 3, 3, 7],
        [9, 3, 5, 2, 4],
        [7, 6, 8, 8, 1],
        [6, 7, 7, 8, 1]])
    print(a)
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
