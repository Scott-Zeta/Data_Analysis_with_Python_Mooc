#!/usr/bin/env python3
import numpy as np
import functools

def matrix_power(a, n):
    m = a.shape[0]
    if(n == 0):
        return np.eye(m)
    if(n < 0):
        a = np.linalg.inv(a)
        n = -n
    power = functools.reduce(np.matmul, (a for n in range(n)), np.eye(m))
    print(power)
    return power

def main():
    a = np.random.randint(0,9,size=(2,2))
    print(a)
    matrix_power(a, 2)

if __name__ == "__main__":
    main()
