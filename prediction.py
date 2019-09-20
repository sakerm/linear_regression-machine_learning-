import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def estimate_price(theta_0, theta_1, x):
	return theta_0 + theta_1 * x

def open_and_save():
    theta = np.zeros((1, 2))
    if (os.path.exists("theta.csv") == False):
        return [0, 0]
    else:
	    theta = np.loadtxt("theta.csv", dtype = np.longdouble, delimiter = ',')
    return theta
    

def main():
    theta = open_and_save()
    try:
		x = np.longdouble(raw_input("Enter a number: "))
    except:
		print ("Error")
		exit()

    print estimate_price(theta[0], theta[1], x)
    if (len(sys.argv) == 2 and sys.argv[1] == "-visual"):
            fsock = open("data.csv", 'r')
            save_file = fsock.readlines()
            i = 1
            xsave = []
            ysave = []
            
            while i != len(save_file):
                r = save_file[i].split(",")
                xsave.append(r[0])   
                ysave.append(r[1])
                i += 1

            plt.plot(xsave, ysave, 'ro')
            plt.plot(x, estimate_price(theta[0], theta[1], x), 'o')
            plt.show()

if __name__ == "__main__":
	main()