import re
import matplotlib.pyplot as plt

if __name__ == '__main__':
    FILENAME = "example.txt"
    names = []
    messages = []
    with open("./" + FILENAME ,  encoding="utf8") as f:
        lines = f.readlines()
        for aaa in lines:
            x = re.search(r'\d{2}.\d{2}.\d{2}, \d{2}:\d{2} - ', aaa)
            if(x is not None):
                if(aaa[x.span()[1]:-1].find(":") != -1):
                    name = aaa[x.span()[1]:-1].split(":")[0]
                    if(name in names):
                        messages[names.index(name)]+=1
                    else:
                        names.append(name)
                        messages.append(1)
    tuple = [(names[aaa],messages[aaa])for aaa in range(len(names))]
    tuple.sort(key=lambda a:-a[1])
    with open("./chart.txt", "w") as f:
        for aaa in range(len(tuple)):
            f.write(str(aaa+1) + ". "+ tuple[aaa][0]+": " + str(tuple[aaa][1]) + "\n")
    plt.rc('font', size=10)
    plt.figure(figsize=(len(tuple)/6+2,len(tuple)/10+3))
    plt.xticks(ticks=range(len([aaa[0] for aaa in tuple])), labels=[aaa[0] for aaa in tuple], rotation=90)
    plt.bar([aaa[0] for aaa in tuple] , [aaa[1] for aaa in tuple])
    plt.tight_layout()
    plt.savefig("./graph.png")
