#!/usr/bin/env python3

import sys
import re

def file_extensions(filename):
    dic = {}
    li = []
    with open(filename,"r") as f:
        count = 1
        for l in f:
            l = l.rstrip()
            print(f"{count}: {l}")
            count+=1
            matches = re.search(r'.+\.[^\.]+', l)
            if(matches != None):
                ex = l.split(".")[-1]
                print(ex)
            else:
                #non_extention()
                li.append(l)
    print(li)
    return ([], {})

def main():
    if(len(sys.argv) > 1):
        file_extensions(sys.argv[1])

if __name__ == "__main__":
    main()
