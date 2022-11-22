#!/usr/bin/env python3

def merge(L1, L2):
    newlist = []
    p1 = 0
    p2 = 0
    while(p1 < len(L1) and p2 < len(L2)):
        if(L1[p1] < L2[p2]):
            newlist.append(L1[p1])
            p1+=1
        else:
            newlist.append(L2[p2])
            p2+=1
    if(p1<len(L1)):
            newlist.extend(L1[p1:])
    if(p2<len(L2)):
            newlist.extend(L2[p2:])
    return newlist

def main():
    list1 = [1,7,9,10]
    list2 = [0,2,4,6,15,20]
    print(merge(list1,list2))

if __name__ == "__main__":
    main()
