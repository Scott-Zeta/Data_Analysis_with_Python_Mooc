#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    row = []
    for n in range(a.shape[0]):
        r = a[n,:]
        row.append(r)
    return row

def get_columns(a):
    col = []
    a = a.T
    for n in range(a.shape[0]):
        r = a[n,:]
        col.append(r)
    return col

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
