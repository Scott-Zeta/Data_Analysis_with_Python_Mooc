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
    for char in s:
        if char not in alphabet:
            return False
    return True

def get_features_and_labels():
    finnish = load_finnish()
    english = load_english()

    finnish = [word.lower() for word in finnish]
    finnish = np.array([word for word in finnish if contains_valid_chars(word)])
    # get rid of word start with upper case
    english = [word for word in english if word[0].islower()]
    english = [word.lower() for word in english]
    english = np.array([word for word in english if contains_valid_chars(word)])
    
    X = get_features(np.concatenate((finnish,english)))
    y = np.zeros((len(X),1))
    y[len(finnish):] = 1
    return X, y


def word_classification():
    return []


def main():
    X,y = get_features_and_labels()
    print(X.shape)
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
