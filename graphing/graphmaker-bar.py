#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 4
    localnetMeans = (20, 35, 30, 35)
    wanMeans = (25, 32, 34, 20)
    ind = np.arange(N)
    width = 0.35

    p1 = plt.bar(ind, localnetMeans, width)
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    plt.savefig("2018summary.png")
    
if __name__ == "__main__":
    main()
