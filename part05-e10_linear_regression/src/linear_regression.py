#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import random

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    return model.coef_[0], model.intercept_
    
def main():
    ran_slope = random.uniform(-3,3)
    ran_inter = random.uniform(-5,5)
    n = 11
    x = np.linspace(0,10,n)
    y = x*ran_slope + ran_inter + np.random.randn(n)
    # print(ran_slope)
    # print(ran_inter)
    slope, intercept = fit_line(x,y)
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    plt.plot(x,y,'o')
    predict_value = [slope*i + intercept for i in x]
    plt.plot(x,predict_value,color = 'red')
    plt.show()
    
if __name__ == "__main__":
    main()
