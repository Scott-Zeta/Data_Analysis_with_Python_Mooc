#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    x1 = [2,4,6,7]
    y1 = [4,3,5,1]
    x2 = [1,2,3,4]
    y2 = [4,2,3,1]

    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.xlabel("My x-axis")       # Give a label to the x-axis
    plt.ylabel("My y-axis")
    plt.show()

if __name__ == "__main__":
    main()
