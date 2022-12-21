#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    height,width,_ = a.shape
    return ((height-1)/2,(width-1)/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    h,w,_ = a.shape
    x,y = np.mgrid[:h,:w] #this will generate two coordinate map of the shape
    # like [[0,1,2] [0,1,2] [0,1,2]] and [[0,0,0] [1,1,1] [2,2,2]]
    centorid = center(a)
    distance = np.sqrt((x-centorid[0])**2 + (y-centorid[1])**2) # use shape map for calculate, avoid for loop
    return distance

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.array([[]])

def radial_mask(a):
    return np.array([[]])

def radial_fade(a):
    return np.array([[]])

def main():
    print(center(np.zeros((5, 5, 3))))
    print(radial_distance(np.zeros((5, 5, 3))))

if __name__ == "__main__":
    main()
