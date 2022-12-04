#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename,'r') as f:
        # if skip the empty lines
        # content = [l.rstrip() for l in f if l.rstrip()]
        content = [l for l in f]
        lines = len(content)
        words = 0
        char = 0
        for l in content:
            line = l.split()
            words += len(line)
            char += len(l)
        print(lines)
        print(words)
        print(char)
    return (lines, words, char)

def main():
    if(len(sys.argv) > 1):
        file_count(sys.argv[1])

if __name__ == "__main__":
    main()
