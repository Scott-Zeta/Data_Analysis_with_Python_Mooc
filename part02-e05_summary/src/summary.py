#!/usr/bin/env python3

import sys
import re
from functools import reduce
import math
import statistics

def summary(filename):
    dataset = []
    with open(filename,"r") as f:
        for line in f:
            matches = re.match(r"-*\d+.?\d*", line)
            if(matches != None):
                dataset.append(matches.group(0))
        sum, avg, std = calculate(dataset)
    return (sum,avg,std)

def calculate(dataset):
    dataset = [float(element) for element in dataset]
    sum = reduce(lambda x,y: x+y,dataset,0)
    avg = sum/len(dataset)
    std = math.sqrt((reduce(lambda x,y: (y - avg)**2 + x,dataset,0))/(len(dataset)-1))
    # std = statistics.stdev(dataset)
    return sum,avg,std

def main():
    filename = sys.argv[1:]
    for name in filename:
        tup = summary(name)
        print(f"File: {name} Sum: {tup[0]:.6f} Average: {tup[1]:.6f} Stddev: {tup[2]:.6f}")

if __name__ == "__main__":
    main()
