#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    matches = re.findall(r'\[[\s]*([-+]*)(\d+)[\s]*\]', s)
    print(matches)
    newTupleList = []
    for elements in matches:
        count = 0
        for i in range(len(elements[0])):
            if(elements[0][i] == "-"):
                count += 1
        if(count%2 == 0):
            newTupleList.append((1,elements[1]))
        else:
            newTupleList.append((-1,elements[1]))
    print(newTupleList)
    result = [i[0] * int(i[1]) for i in newTupleList]
    #print(result)
    return result

def main():
    print(integers_in_brackets("afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"))

if __name__ == "__main__":
    main()
