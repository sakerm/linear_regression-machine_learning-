import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys
from string import *
import sys
import argparse
import math
import os

xsave = [] 
ysave = []
thetaSavex = []
thetaSavey = []

def save_theta(theta, x, y):
	a = (y[0] - y[1]) / (x[0] - x[1])
	b = a * x[0] * -1 + y[0]
	theta = [b, a]
	np.savetxt("theta.csv", theta, delimiter = ',')

def save_value():
    if (os.path.exists("data.csv") == False or len(sys.argv) != 2):
        exit()
    if (sys.argv[1] != "data.csv"):
        exit()
    save = sys.stdin
    fsock = open(sys.argv[1], 'r')
    save_file = fsock.readlines()

    i = 1

    while i != len(save_file):
        r = save_file[i].split(",")
        xsave.append(atoi(r[0]))   
        ysave.append(atoi(r[1]))
        i += 1

    plt.plot(xsave, ysave, 'ro')
    return(save_file)

def estimate_price(theta_0, theta_1, x):
        return theta_0 + theta_1 * x

def compute_gradients(x, y, m, theta, alpha, iterations):
    i = 0
    while i != iterations: #range(0, iterations):
        tmp_theta = np.zeros((1, 2))
        for j in range(0, m):
            tmp_theta[0, 0] += (estimate_price(theta[0, 0], theta[0, 1], x[j]) - y[j])
            tmp_theta[0, 1] += ((estimate_price(theta[0, 0], theta[0, 1], x[j]) - y[j]) * x[j])
        theta -= (tmp_theta * alpha) / m
        i += 1
    return theta

def standardize(x):
    return (x - np.mean(x)) / np.std(x)

def destandardize(x, x_ref):
    return x * np.std(x_ref) + np.mean(x_ref)

def main():
    save_file = save_value()
    m = len(save_file) - 1
    x = standardize(xsave)
    y = standardize(ysave)
    theta = np.zeros((1, 2))
    alpha = 0.3
    iteration = 20
    theta = compute_gradients(x, y, m, theta, alpha, iteration)
    y = estimate_price(theta[0, 0], theta[0, 1], x)
    x = destandardize(x, xsave)
    y = destandardize(y, ysave)
    save_theta(theta, x, y)
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()