#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    height = (a.shape[0]-1)/2
    width = (a.shape[1]-1)/2
    return (height,width)   # note the order: (center_y, center_x)

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
    scaled_a = np.interp(a,(a.min(),a.max()),(tmin,tmax))
    return scaled_a

def radial_mask(a):
    result = scale(1-radial_distance(a))
    return result

def radial_fade(a):
    return a * radial_mask(a)[...,np.newaxis] #add a new dimension 

def main():
    a = np.random.randint(0,11,size=(3,3))
    print(center(np.zeros((5, 5, 3))))
    print(radial_distance(np.zeros((5, 5, 3))))
    print(a)
    print(scale(a))
    image = plt.imread("src/painting.png").copy()
    f, ax = plt.subplots(3,1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image),cmap=plt.get_cmap('gray'))
    ax[2].imshow(radial_fade(image))
    plt.show()

if __name__ == "__main__":
    main()
