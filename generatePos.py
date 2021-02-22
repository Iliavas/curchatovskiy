class GenerateGrid:
    sizes = []
    vertex = set()
    vectors = [
        [1,1,1],
        [-1,-1,1],
        [-1,-1,-1],
        [1,1,-1],
        [-1,1,-1],
        [-1,1,1],
        [1,-1,-1],
        [1,-1,1]
    ]
    def __init__(self, posx, posy, posz):
        sizes = [posx, posy, posz]
        self.vertex.add((0,0,0))
        
        have_unordered_vert = True
        
        stack = [[0, 0, 0]]

        while len(stack):
            pos = stack[0]
            stack.pop(0)
            for i in self.vectors:
                pot_pos = (i[0]+pos[0], i[1]+pos[1], i[2]+pos[2])
                if pot_pos in self.vertex:
                    self.vertex.add(pot_pos)
                    stack.append(pot_pos)
    

    def is_affilate(self, posx, posy, posz):
        if [posx, posy, posz] in self.vertex:
            return True
        return False
