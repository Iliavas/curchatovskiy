from time import time

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def draw(data):
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.plot(*data)
    plt.savefig(str(time())+".png")
    
