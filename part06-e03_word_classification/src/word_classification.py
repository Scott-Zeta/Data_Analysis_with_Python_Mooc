#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

# Warning, letter out of alphabet will be skiped
def get_features(a):
    alphabetDic = {alphabet[i]:i for i in range(29)}
    feature = np.zeros((len(a),29))
    for i,word in enumerate(a):
        for char in word:
            if char in alphabet:
                feature[i,alphabetDic[char]] += 1
    print(feature)
    return feature

def contains_valid_chars(s):
    return True

def get_features_and_labels():
    return np.array([[]]), np.array([])


def word_classification():
    return []


def main():
    get_features(np.array(["hello", "hell", "world"]))
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
