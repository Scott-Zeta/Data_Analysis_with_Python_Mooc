#!/usr/bin/env python3

def reverse_dictionary(d):
    rDict = {}
    for i in d:
        # print(i)
        for j in d[i]:
            # print(j)
            if j in rDict:
                rDict[j].append(i)
            else:
                rDict.update({j:[i]})

    return rDict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
