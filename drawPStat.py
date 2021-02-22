import matplotlib.pyplot as plt

#from scipy import stats

class DrawP:
    def __init__(self, p):
        self.accelerator = {p:[]}
        self.p = p
    
    
    def countFunction(self, countList):
        res = 0
        try:
            res = sum(map(lambda x : (6)/(x*3.0+1), countList)) / len(countList)
        except:
            pass
        return res

    
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
        #sem = stats.sem(list(self.accelerator.values()))
        #print(sem)
        #print(list(self.accelerator.keys()), list(self.accelerator.values()),"keys")
        #plt.errorbar(list(self.accelerator.keys()), list(self.accelerator.values()),
                     #sem, mfc="red", marker="s", mec="green")

        #plt.savefig("b.png")

        plt.hist(self.accelerator.values(), color="b", bins=50)
        plt.savefig("c.png")
d = DrawP(0.1)

d.append(10)
d.change_p(0.2)
d.append(10)
d.change_p(0.3)
d.append(30)
d.draw()