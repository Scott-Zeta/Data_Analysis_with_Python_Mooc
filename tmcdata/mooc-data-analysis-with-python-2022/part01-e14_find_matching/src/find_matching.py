#!/usr/bin/env python3

def find_matching(L, pattern):
    
    result = []
    for i,x in enumerate(L):
        if(x.find(pattern) != -1):
            result.append(i)
    return result

def main():
    s = ["sensitive", "engine", "rubbish", "comment"]
    print(find_matching(s, "en"))

if __name__ == "__main__":
    main()
