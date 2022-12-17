#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a = np.arange(n)
    b= np.arange(n).reshape(n,1)
    print(a)
    print(b)
    broadA, broadB = np.broadcast_arrays(a,b)
    print(broadA)
    print(broadB)
    result = np.multiply(broadA,broadB)
    return result

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
