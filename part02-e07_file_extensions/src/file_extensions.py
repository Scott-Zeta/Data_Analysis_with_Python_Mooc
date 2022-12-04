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
                if ex in dic:
                    dic[ex].append(l)
                else:
                    dic[ex] = []
                    dic[ex].append(l)
            else:
                #non_extention()
                li.append(l)
    # print(li)
    # print(dic)
    return (li, dic)

def main():
    filename = ""
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
    tp = file_extensions(filename)
    # print(tp)
    print(f"{len(tp[0])} files with no extension")
    for li in sorted(tp[1]):
        print(f'{li} {len(tp[1][li])}')
    
        

if __name__ == "__main__":
    main()
