#!/usr/bin/env python3

def triple(num):
    return num*3

def square(num):
    return num ** 2

def main():
    for i in range(1,11):
        s = square(i)
        t = triple(i)
        if(t >= s):
            print(f"triple({i})=={t} square({i})=={s}")
        else:
            break

if __name__ == "__main__":
    main()
