from Point import Point
from Stok import Stok
from time import sleep
import numpy as np

from utils import dist, randomize

class Vertex:

  accelerator = []

  def __init__(self, sizex, sizey, sizez, pointsLen, stokLen, stokR):
    self.vertex = [sizex, sizey, sizez]

    self.stoks = [
        Stok(randomize(sizex, sizey, sizez, lambda x,y,z: True), stokR)
        for _ in range(0, stokLen)
    ]

    self.points = [
        Point(randomize(sizex, sizey, sizex, self.is_normal_positioned))
        for _ in range(0, pointsLen)
    ]
    print(self.stoks)
    print(self.points)

    self.stok_pos = [sizex/2, sizey/2, sizez/2]
    self.R = stokR
  
  def affilate(self, size):
    response = not len(list(filter(lambda x : x, map(lambda x: x < 0, size))))
    for i in range(0, 3):
      if self.vertex[i] < size[i]: response = False
    
    return response
  

  def tick(self):
    for i in self.points:
      i.tick(np.random.random())
      i.x = i.x % self.vertex[0]
      i.y = i.y % self.vertex[1]
      i.z = i.z % self.vertex[2]
      if i.x < 0: i.x = self.vertex[0]
      if i.y < 0: i.y = self.vertex[1]
      if i.z < 0: i.z = self.vertex[2]

      self.is_stok(i)

  def simulate(self, period):
      while True:
        #sleep(period)
        self.tick()
        #print()
  
  def is_stok(self, point:Point):
    if dist(point.x, point.y, point.z, *self.stok_pos) < self.R:
      self.accelerator.append(point.counter)
      point.set_stok(True)
      pos = randomize(*self.vertex)
      point.x = pos[0]
      point.y = pos[1]
      point.z = pos[2]
    else:
      point.set_stok(False)
  
  def is_normal_positioned(self, x, y, z):
    for stok in self.stoks:
        if dist(stok.x, stok.y, stok.z, x, y, z) < stok.R:
            return False
    return True
  

  def __repr__(self):
    return "Vertex: ([{}])".format(", ".join(map(lambda x : str(x), self.vertex)))