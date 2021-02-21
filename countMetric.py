import matplotlib.pyplot as plt

with open("res.txt", "r") as file:
    metric = list((map(lambda x : 6 / (int(x) * 3), file.read().split())))
    a = dict()
    for i in metric:
        if i in a.keys():
            a[i]+=1
        else:
            a.update({i:1})
    plt.bar(list(a.keys()), list(a.values()))
    plt.savefig("a.png")