import numpy as np

def dist(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2) ** 0.5


def randomize(x, y, z, pos_f):
    x, y, z = 0, 0, 0 
    while True:
        x, y, z = int(np.random.random() * x), int(np.random.random() * y), int(np.random.random() * z)
        if pos_f(x,y,z): break
    
    return (x, y, z)