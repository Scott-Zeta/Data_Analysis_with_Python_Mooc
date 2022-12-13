#!/usr/bin/env python3
 
import numpy as np
 
def diamond(n):
    e=np.eye(n, dtype=int)
    print(e)
    print("--------------")
    a=np.concatenate([e[::-1], e[:,1:]], axis=1)
    print(a)
    print("-------------------")
    result = np.concatenate([a[:-1], a[::-1]], axis=0)
    return result
 
def main():
    print(diamond(3))
 
if __name__ == "__main__":
    main()