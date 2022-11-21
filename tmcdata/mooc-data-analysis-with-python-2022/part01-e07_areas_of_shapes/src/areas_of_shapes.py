#!/usr/bin/env python3

import math

def rec():
    b = float(input("Give width of the rectangle: "))
    h = float(input("Give height of the rectangle: "))
    return float(b*h)
def tri():
    b = float(input("Give base of the triangle: "))
    h = float(input("Give height of the triangle: "))
    return float(b*h*1/2)
def cir():
    r = float(input("Give radius of the circle: "))
    return math.pi * (r ** 2)

def main():
    # enter you solution here
    while(True):
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if(shape == ""):
            break
        elif(shape == "triangle"):
            area = tri()
        elif(shape == "rectangle"):
            area = rec()
        elif(shape == "circle"):
            area = cir()
        else:
            print("Unknown shape!")
            continue
        print(f"The area is {area}")

if __name__ == "__main__":
    main()
