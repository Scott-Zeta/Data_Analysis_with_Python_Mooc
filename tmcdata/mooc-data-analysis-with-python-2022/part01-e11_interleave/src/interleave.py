#!/usr/bin/env python3

def interleave(*lists):
    x1= []
    x2= []
    zip(x1,x2)
    result = []
    for j in range(len(lists[0])):
        for i in range(len(lists)):
            result.append(lists[i][j])
    return result

def main():
    print(list(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c'])))

if __name__ == "__main__":
    main()
