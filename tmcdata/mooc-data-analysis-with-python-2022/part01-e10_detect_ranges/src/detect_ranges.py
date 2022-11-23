#!/usr/bin/env python3

def detect_ranges(L):
    sortedList = sorted(L)
    rangeList = []
    p1 = 0
    p2 = 0
    while(p1 < len(sortedList) and p2 < len(sortedList)):
        if(p2 < len(sortedList) -1  and sortedList[p2] + 1 == sortedList[p2 + 1]):
            p2+=1
        else:
            if(p1 == p2):
                rangeList.append(sortedList[p1])
            else:
                rangeList.append((sortedList[p1],sortedList[p2] + 1))
            p2 += 1
            p1 = p2
        print(rangeList)
    return rangeList

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    print(sorted(L))
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
