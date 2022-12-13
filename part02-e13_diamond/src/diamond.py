#!/usr/bin/env python3

import numpy as np

def diamond(n):
    dim = n*2 - 1
    d = np.zeros((dim,dim), dtype = int)
    trick = np.eye(dim)
    trick2 = np.arange(2)
    trick2 = np.concatenate((trick2,trick2))
    for n in range(d.shape[1]):
        if (n < int(dim/2)):
            d[n,int(dim/2)+n] = 1
            d[n,int(dim/2)-n] = 1
        else:
            d[n,int(dim/2)+(dim-n-1)] = 1
            d[n,int(dim/2)-(dim-n-1)] = 1
    return d

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
