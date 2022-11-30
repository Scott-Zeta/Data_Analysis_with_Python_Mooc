#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    matches = re.findall(r'\[[\s]*([-+]?\d+)[\s]*\]', s)
    print(matches)
    result = [int(i) for i in matches]
    print(result)
    return result

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx [+-43]"))

if __name__ == "__main__":
    main()
