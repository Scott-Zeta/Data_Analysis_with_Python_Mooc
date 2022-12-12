#!/usr/bin/env python3

def extract_numbers(s):
    li = []
    input = s.split()
    for e in input:
        try:
            li.append(int(e))
        except:
            try:
                li.append(float(e))
            except:
                continue
    return li

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
