#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename,"r") as f:
        lines = f.readlines()
    count = 1
    result = []
    for i in range(len(lines)):
        if (i == 0):
            continue
        matches = re.match(r"\s*(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)", lines[i])
        print(f"{count}: R:{matches.group(1)} G:{matches.group(2)} B:{matches.group(3)} Name:{matches.group(4)}")
        strElement=""
        for i in range(1,5):
            if(i == 4):
                strElement += f"{matches.group(i)}"
            else:    
                strElement += f"{matches.group(i)}\t"
        print(strElement)
        result.append(strElement)
        count +=1
    return result

# better solution
def red_green_blue(filename="src/rgb.txt"):
    with open(filename) as in_file:
        l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())
        return [
            "{}\t{}\t{}\t{}".format(r, g, b, name)
            for r, g, b, name
            in l
        ]


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
