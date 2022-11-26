#!/usr/bin/env python3
from functools import reduce

def sum_equation(L):
    if(L == []):
        return "0 = 0"
    sum = reduce(lambda x,y:x+y, L, 0)
    #print(sum)
    stringL = [str(x) for x in L]
    stringL = " + ".join(stringL)
    return f"{stringL} = {sum}"

def main():
    print(sum_equation([1,4,6,8,10]))

if __name__ == "__main__":
    main()
