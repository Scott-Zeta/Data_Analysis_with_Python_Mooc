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

# alternative way to read the file
def word_frequencies(filename = "src/alice.txt"):
    result = {}
    with open(filename) as in_file:
        for w in in_file.read().split():
            ws = w.strip("""!"#$%&'()*,-./:;?@[]_""")
            if ws not in result:
                result[ws] = 0
            result[ws] += 1
    return result


def main():
    dic = word_frequencies()
    print(dic)

if __name__ == "__main__":
    main()
