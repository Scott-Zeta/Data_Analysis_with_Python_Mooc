#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

def plant_classification():
    iris = load_iris()
    X = iris.data
    y = iris.target
    model = GaussianNB()
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)
    model.fit(X_train,y_train)
    y_fitted = model.predict(X_test)
    accuracy = metrics.accuracy_score(y_fitted,y_test)
    return accuracy

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
