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

def interleave(*lists):
    # to zip multiple list, 
    # use The strange looking argument notation (the star) is called argument packing
    result = []
    print(list(zip(*lists)))
    for t in zip(*lists):
        result.extend(t)
        print(result)
    return result

def main():
    print(list(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c'])))

if __name__ == "__main__":
    main()
