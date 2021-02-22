import numpy as np

from graphDrawer import draw

class Point:
  counter = 0
  global_counter = 0


  def __init__(self, pos):
    self.x = pos[0]
    self.y = pos[1]
    self.z = pos[2]
    self.is_stok = False
    self.xs = [pos[0]]
    self.ys = [pos[1]]
    self.zs = [pos[2]]

  def tick(self, p):
    zero_one_interval = [0, p]
    average = (1 - p)/2
    one_two_interval = [p, p+average]
    two_three_interval = [p+average, p+2*average]
    three_four_interval = [p+2*average, 1]
    intervals = [zero_one_interval, one_two_interval, two_three_interval, three_four_interval]
    
    first_rand = np.random.random()
    interval = 0
    for i in enumerate(intervals):
      if first_rand >= i[1][0] and first_rand < i[1][1]: interval = i[0]
    
    potential_force = [
         [[-1,1,1],[1,-1,-1]],
         [[1,1,1],[-1,-1,-1]],
         [[1,-1,1],[-1,1,-1]],
         [[-1,-1,1],[1,1,-1]]
    ]

    second_rand = np.random.random()
    is_up = 0
    if second_rand > 0.5: is_up = 1
    force = potential_force[interval][is_up]
    self.x += force[0]
    self.y += force[1]
    self.z += force[2]
    self.counter+=1
    self.xs.append(self.x)
    self.ys.append(self.y)
    self.zs.append(self.z)

    #if self.counter >= 1000:
    #    draw([self.xs, self.ys, self.zs])
    #print(self, self.counter)
            

  def __str__(self):
    return "Point({0}, {1}, {2}, stok: {3})".format(self.x, self.y, self.z, self.is_stok)
  

  def set_stok(self, stokState):
    if (stokState == True): 
        with open("res.txt", "a") as file:
            file.write(str(self.counter) + " ")
        with open("res.txt", "r") as file:
            if len(file.read().split(" ")) >= 5000: exit(0)
        counter_bin = self.counter
        self.counter = 0
        draw([self.xs, self.ys, self.zs])
        self.xs = []
        self.ys = []
        self.zs = []
        self.global_counter += 1

        return counter_bin

    self.is_stok = stokState
  

  def __repr__(self):
    return "Point ({}, {}, {})".format(self.x, self.y, self.z)