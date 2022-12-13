#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    row = []
    news = np.split(a, a.shape[0])
    for i,p in enumerate(news):
        row.append(p)
    return row

def get_column_vectors(a):
    col = []
    news = np.split(a, a.shape[1],axis =1)
    for i,p in enumerate(news):
        col.append(p)
    return col

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
