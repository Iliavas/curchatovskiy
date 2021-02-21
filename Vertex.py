from Point import Point
from time import sleep
import numpy as np

class Vertex:
  def __init__(self, sizex, sizey, sizez, pointsLen):
    self.vertex = [sizex, sizey, sizez]
    self.points = [
        Point([np.random.random() * sizex, np.random.random() * sizey, np.random.random() * sizez])
        for _ in range(0, pointsLen) 
    ]
  
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

  def simulate(self, period):
      while True:
        sleep(period)
        self.tick()
        print()
  

  def __repr__(self):
    return "Vertex: ([{}])".format(", ".join(map(lambda x : str(x), self.vertex)))