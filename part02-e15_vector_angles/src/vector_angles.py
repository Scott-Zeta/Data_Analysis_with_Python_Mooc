#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
     #Find dot product for the numerator
    prod = np.multiply(X,Y)
    dotProduct = np.sum(prod)
    # dotProduct = np.dot(X,Y)

    #find the norm of both X and Y
    normX = np.sqrt(np.sum(np.square(X)))
    normY = np.sqrt(np.sum(np.square(Y)))

    #This gives the whole fraction
    fraction = dotProduct/(np.multiply(normX,normY))
    print(fraction)
    # cos value reverse to angle
    angle = np.arccos(fraction)
    print(angle)

    #changing from degrees to radians
    # angle to radians (the length of unit 1 circle)
    result = angle*180/np.pi
    print(result)
    return np.array(result)

def main():
    a = np.array([1,2,3])
    b = np.array([2,3,4])
    vector_angles(a, b)
if __name__ == "__main__":
    main()
