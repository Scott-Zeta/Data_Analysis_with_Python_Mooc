#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
     #Find dot product for the numerator
    prod = np.multiply(X,Y)
    dotProduct = np.sum(prod)

    #find the norm of both X and Y
    normX = np.sqrt(np.sum(np.square(X)))
    normY = np.sqrt(np.sum(np.square(Y)))

    #This gives the whole fraction
    fraction = dotProduct/(np.multiply(normX,normY))
    angle = np.arccos(fraction)

    #changing from degrees to radians
    result = angle*180/np.pi
    return np.array(result)

def main():
    a = np.array([1,2,3])
    b = np.array([2,3,4])
    vector_angles(a, b)
if __name__ == "__main__":
    main()
