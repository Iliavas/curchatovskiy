import matplotlib.pyplot as plt

class DrawP:
    def __init__(self, p):
        self.accelerator = {p:[]}
        self.p = p
    
    
    def countFunction(self, countList):
        return sum(map(lambda x : (6)/(x*3.0+1), countList)) / len(countList)

    
    def append(self, v):
        print(self.accelerator, self.p)
        self.accelerator[self.p].append(v)
    

    def __len__(self):
        return len(self.accelerator[self.p])
    

    def change_p(self, new_p):
        self.accelerator.update({new_p:[]})
        self.p = new_p

    def draw(self):
        for i in self.accelerator.keys():
            self.accelerator[i] = self.countFunction(self.accelerator[i])
        print(list(self.accelerator.keys()), list(self.accelerator.values()))
        plt.plot(self.accelerator.keys(), self.accelerator.values())
        plt.savefig("a.png")