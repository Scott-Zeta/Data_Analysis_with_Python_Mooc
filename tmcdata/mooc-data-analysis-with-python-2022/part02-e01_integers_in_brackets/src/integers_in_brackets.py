#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    s1 = re.findall([.], s)
    return s1

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
