import numpy as np

def dist(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2) ** 0.5


def randomize(x, y, z, pos_f):
    while True:
        x_, y_, z_ = int(np.random.random() * x), int(np.random.random() * y), int(np.random.random() * z)
        print(pos_f(x_, y_, z_), x_, y_,z_)
        if pos_f(x_,y_,z_): return (x_, y_, z_)