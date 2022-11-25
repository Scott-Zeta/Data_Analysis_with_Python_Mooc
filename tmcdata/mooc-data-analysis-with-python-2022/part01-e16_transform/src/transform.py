#!/usr/bin/env python3


def transform(s1, s2):
    newlist = zip([int(i) for i in s1.split()],[int(i) for i in s2.split()])
    # split default seperator is any white space " ", "\t" etc.
    # print(list(map(lambda x: x[0]*x[1], newlist)))
    return list(map(lambda x: x[0]*x[1], newlist))

def main():
    result = transform("1 5 3", "2 6 -1")
    print(result)

if __name__ == "__main__":
    main()
