#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_red(img):
    result = img.copy()
    result[...,(1,2)] = 0
    return result
def to_green(img):
    result = img.copy()
    result[...,(0,2)] = 0
    return result
def to_blue(img):
    result = img.copy()
    result[...,(0,1)] = 0
    return result

def to_grayscale(img):
    result = np.dot(img[...,:3],[0.2126, 0.7152, 0.0722])
    return result

def main():
    image = plt.imread("src/painting.png")
    print(image.shape)
    grayImg = to_grayscale(image)
    plt.imshow(grayImg,cmap=plt.get_cmap('gray'))

    fig, ax = plt.subplots(3,1)
    ax[0].imshow(to_red(image))
    ax[1].imshow(to_green(image))
    ax[2].imshow(to_blue(image))
    plt.show()

if __name__ == "__main__":
    main()
