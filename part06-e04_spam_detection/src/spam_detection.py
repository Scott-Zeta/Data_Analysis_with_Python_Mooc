#!/usr/bin/env python3
from gzip import open
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np 

def spam_detection(random_state=0, fraction=1.0):
    with open("src/ham.txt.gz") as data:
        list_hame = data.readlines()
    with open("src/spam.txt.gz") as data:
        list_spam = data.readlines()
    
    # slice the data in fraction given
    list_hame = list_hame[:int(fraction*len(list_hame))]
    list_spam = list_spam[:int(fraction*len(list_spam))]

    # Build the data X
    vec = CountVectorizer()
    list_X = list_hame + list_spam
    X = vec.fit_transform(list_X)
    # give label y
    y = np.zeros(len(list_X))
    y[:len(list_hame)] = 1

    #split the data
    X_train,X_test,y_train,y_test = train_test_split(X,y,train_size = 0.75 ,shuffle = True, random_state=random_state)
    #Build the model
    model = MultinomialNB()
    model.fit(X_train,y_train)
    # get the prediction
    y_fitted = model.predict(X_test)
    # accuracy result and misclassified number
    accu = accuracy_score(y_test,y_fitted)
    missclasified = (y_test != y_fitted).sum()
    return (accu, len(y_test), missclasified)

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
