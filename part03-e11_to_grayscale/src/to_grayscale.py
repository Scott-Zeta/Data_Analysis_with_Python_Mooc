#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    result = np.dot(img[...,:3],[0.2126, 0.7152, 0.0722])
    return result

def main():
    image = plt.imread("src/painting.png")
    print(image.shape)
    grayImg = to_grayscale(image)
    plt.imshow(grayImg)
    plt.show()

if __name__ == "__main__":
    main()
