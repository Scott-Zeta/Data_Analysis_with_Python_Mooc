#!/usr/bin/env python3

import pandas as pd

def read_series():
    valueList = []
    indexList = []
    while(True):
        userInput = input("Type, asshole: ")
        if(userInput == ""):
            break
        else:
            try:
                index, value = userInput.split()
                valueList.append(value)
                indexList.append(index)
            except:
                print("invalid input")
    return pd.Series(valueList,index=indexList)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
