class Stok:
    def __init__(self, pos, R):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.R = R
    

    def __repr__(self):
        return "Stok([{}, {}, {}, R: {}])".format(self.x, self.y, self.z, self.R)