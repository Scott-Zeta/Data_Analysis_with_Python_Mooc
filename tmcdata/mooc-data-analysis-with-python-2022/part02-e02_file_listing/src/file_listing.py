#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    count = 1
    result = []
    with open(filename,"r") as f:
        lines = f.readlines()
    for line in lines:
        print(f'{count}: {line}',end="")
        matches = re.findall(r'(\d+)\s+(\w{3})\s+(\d{1,2})\s+(\d{2}):(\d{2})\s+([.\w]+.\w+)', line)
        print(matches[0])
        
        # another solution of digits string elements to Integer
        toIntTuple = (int(element) if element.isdecimal() else element for element in matches[0])
        print(list(toIntTuple))
        
        
        intTuple = ()
        for element in matches[0]:
            if element.isnumeric():
                intTuple += (int(element),)
            else:
                intTuple += ((element),)
        result.append(intTuple)
        count +=1
    print(result)
    return result

def main():
    file_listing()

if __name__ == "__main__":
    main()
