from tiny_3d_engine import (Scene3D, Engine3D)


class Position:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]


class Cube:
    def __init__(self, pos, size, name, scene):
        self.ini(pos, size, name, scene)

    def ini(self, pos, size, name, scene):
        self.pos = pos
        self.size = size
        self.name = name

        points = list()
        conn = list()

        points.append([pos.x - size, pos.y - size, pos.z])  # 0
        points.append([pos.x, pos.y - size, pos.z])  # 1
        points.append([pos.x - size, pos.y, pos.z])  # 2
        points.append([pos.x, pos.y, pos.z])  # 3
        points.append([pos.x, pos.y - size, pos.z - size])  # 4
        points.append([pos.x, pos.y, pos.z - size])  # 5
        points.append([pos.x - size, pos.y, pos.z - size])  # 6
        points.append([pos.x - size, pos.y - size, pos.z - size])  # 7

        conn.append([0, 1, 3, 2])
        conn.append([0, 1, 4, 7])
        conn.append([3, 2, 6, 5])
        conn.append([0, 2, 6, 7])
        conn.append([1, 3, 5, 4])
        conn.append([4, 7, 6, 5])

        self.scn = scene
        self.scn.update(name, points, conn, color="#ff0000")

    def translate(self, pos):
        self.ini(pos, self.size, self.name, self.scn)


class Drawer():
    def __init__(self):
        self.scene = Scene3D()
    def translate(self, numCube, pos):
        self.scene = Cube(pos=pos, size=self.sizeCube, name="sq" + str(numCube), scene=self.scene).scn

    def task1(self, sizeCube, sizePlane):
        size = sizeCube
        self.sizeCube=sizeCube
        x = 0
        y = 0
        z = 0
        sq=0
        for k in range(sizePlane[2]):
            z += (3 * size)
            y = 0
            for i in range(sizePlane[1]):
                y += 3 * size
                if i % 2 == 0:
                    x = 0
                else:
                    x = size
                for j in range(sizePlane[0]):
                    x += 3 * size
                    sq+=1
                    self.scene = Cube(Position((x, y, z)), size, "sq"+str(sq), self.scene).scn

    def update(self):
        test = Engine3D(self.scene)
        test.rotate("x", 45)
        test.rotate("y", 45)
        test.render()
        test.mainloop()


dr = Drawer()

dr.task1(10, (4, 4, 3))
dr.update()

dr.translate(1, Position((300,300,0)))
dr.update()

