#!/usr/bin/env python3

def word_frequencies(filename = "src/alice.txt"):
    result = {}
    with open(filename,"r") as f:
        for line in f:
            #tips for skip the empty lines
            if line.rstrip():
                line = line.split()
                for word in line:
                    word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                    if word in result:
                        result[word] += 1
                    else:
                        result[word] = 1
    return result

def main():
    dic = word_frequencies()
    print(dic)

if __name__ == "__main__":
    main()
