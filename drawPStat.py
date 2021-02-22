import matplotlib.pyplot as plt

from scipy import stats

class DrawP:
    def __init__(self, p):
        self.accelerator = {p:[]}
        self.p = p
    
    
    def countFunction(self, countList):
        count = 0
        try:
            count = sum(map(lambda x : (6)/(x*3.0+1), countList)) / len(countList)
        except:
            pass
        return count

    
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
        sem = stats.sem(list(self.accelerator.values()))
        print(sem)
        print(list(self.accelerator.keys()), list(self.accelerator.values()),"keys")
        plt.errorbar(list(self.accelerator.keys()), list(self.accelerator.values()),
                     sem, mfc="red", marker="s", mec="green")

        plt.savefig("b.png")
