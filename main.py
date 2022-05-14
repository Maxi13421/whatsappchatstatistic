import re
import matplotlib.pyplot as plt

if __name__ == '__main__':
    EXCLUDEDMEDIA = " <Medien ausgeschlossen>"
    DELETEDMESSAGE = [" Du hast diese Nachricht gelöscht.",
                      " Diese Nachricht wurde gelöscht."]
    FILENAME = "example.txt"
    names = []
    messages = []
    messageswithoutmedia = []
    symbols = []
    deletedmessages = []
    with open("./" + FILENAME, encoding="utf8") as f:
        lines = f.readlines()
        for aaa in lines:
            x = re.search(r'\d{2}.\d{2}.\d{2}, \d{2}:\d{2} - ', aaa)
            if(x is not None):
                if(aaa[x.span()[1]:-1].find(":") != -1):
                    name = aaa[x.span()[1]:-1].split(":")[0]
                    message = aaa[x.span()[1]:-1].split(":")[1]
                    if(message not in DELETEDMESSAGE):
                        if(name in names):
                            messages[names.index(name)]+=1
                            if(message!=EXCLUDEDMEDIA):
                                messageswithoutmedia[names.index(name)] += 1
                                symbols[names.index(name)]+=len(message)
                        else:
                            names.append(name)
                            messages.append(1)
                            deletedmessages.append(0)
                            if(message != EXCLUDEDMEDIA):
                                messageswithoutmedia.append(1)
                                symbols.append(len(message))
                            else:
                                messageswithoutmedia.append(0)
                                symbols.append(0)
                    else:
                        if (name in names):
                            deletedmessages[names.index(name)] += 1
                        else:
                            deletedmessages.append(1)
            else:
                symbols[names.index(name)] += len(aaa)


    tuplemessages = [(names[aaa], messages[aaa]) for aaa in range(len(names))]
    tuplesymbols = [(names[aaa], symbols[aaa]) for aaa in range(len(names))]
    tupleaverage = []
    for aaa in range(len(names)):
        if(messageswithoutmedia[aaa]!=0):
            tupleaverage.append((names[aaa], symbols[aaa] / messageswithoutmedia[aaa]))
        else:
            tupleaverage.append((names[aaa], 0.0))
    tuplemedia = [(names[aaa], messages[aaa]-messageswithoutmedia[aaa]) for aaa in range(len(names))]
    tupledeletedmessages = [(names[aaa], deletedmessages[aaa]) for aaa in range(len(names))]
    tuplemessages.sort(key=lambda a:-a[1])
    tuplesymbols.sort(key=lambda a: -a[1])
    tupleaverage.sort(key=lambda a: -a[1])
    tuplemedia.sort(key=lambda a: -a[1])
    tupledeletedmessages.sort(key=lambda a: -a[1])
    with open("./charts/chartmessages.txt", "w") as f:
        for aaa in range(len(tuplemessages)):
            f.write(str(aaa+1) + ". " + tuplemessages[aaa][0] + ": " + str(tuplemessages[aaa][1]) + "\n")
    with open("./charts/chartsymbols.txt", "w") as f:
        for aaa in range(len(tuplesymbols)):
            f.write(str(aaa+1) + ". " + tuplesymbols[aaa][0] + ": " + str(tuplesymbols[aaa][1]) + "\n")
    with open("./charts/chartaveragesymbolspermessage.txt", "w") as f:
        for aaa in range(len(tupleaverage)):
            f.write(str(aaa+1) + ". " + tupleaverage[aaa][0] + ": " + str(tupleaverage[aaa][1]) + "\n")
    with open("./charts/chartmedia.txt", "w") as f:
        for aaa in range(len(tuplemedia)):
            f.write(str(aaa+1) + ". " + tupleaverage[aaa][0] + ": " + str(tuplemedia[aaa][1]) + "\n")
    with open("./charts/chartdeletedmessages.txt", "w") as f:
        for aaa in range(len(tupledeletedmessages)):
            f.write(str(aaa+1) + ". " + tupledeletedmessages[aaa][0] + ": " + str(tupledeletedmessages[aaa][1]) + "\n")
    plt.rc('font', size=10)
    plt.figure(figsize=(len(tuplemessages) / 6 + 2, len(tuplemessages) / 10 + 3))
    plt.xticks(ticks=range(len([aaa[0] for aaa in tuplemessages])), labels=[aaa[0] for aaa in tuplemessages], rotation=90)
    plt.bar([aaa[0] for aaa in tuplemessages], [aaa[1] for aaa in tuplemessages])
    plt.tight_layout()
    plt.savefig("./graphs/graphmessages.png")
    plt.clf()
    plt.rc('font', size=10)
    plt.figure(figsize=(len(tuplesymbols) / 6 + 2, len(tuplesymbols) / 10 + 3))
    plt.xticks(ticks=range(len([aaa[0] for aaa in tuplesymbols])), labels=[aaa[0] for aaa in tuplesymbols],
               rotation=90)
    plt.bar([aaa[0] for aaa in tuplesymbols], [aaa[1] for aaa in tuplesymbols])
    plt.tight_layout()
    plt.savefig("./graphs/graphsymbols.png")
    plt.clf()
    plt.rc('font', size=10)
    plt.figure(figsize=(len(tupleaverage) / 6 + 2, len(tupleaverage) / 10 + 3))
    plt.xticks(ticks=range(len([aaa[0] for aaa in tupleaverage])), labels=[aaa[0] for aaa in tupleaverage],
               rotation=90)
    plt.bar([aaa[0] for aaa in tupleaverage], [aaa[1] for aaa in tupleaverage])
    plt.tight_layout()
    plt.savefig("./graphs/graphsymbolspermessage.png")
    plt.clf()
    plt.rc('font', size=10)
    plt.figure(figsize=(len(tuplemedia) / 6 + 2, len(tuplemedia) / 10 + 3))
    plt.xticks(ticks=range(len([aaa[0] for aaa in tuplemedia])), labels=[aaa[0] for aaa in tuplemedia],
               rotation=90)
    plt.bar([aaa[0] for aaa in tuplemedia], [aaa[1] for aaa in tuplemedia])
    plt.tight_layout()
    plt.savefig("./graphs/graphmedia.png")
    plt.clf()
    plt.rc('font', size=10)
    plt.figure(figsize=(len(tupledeletedmessages) / 6 + 2, len(tupledeletedmessages) / 10 + 3))
    plt.xticks(ticks=range(len([aaa[0] for aaa in tupledeletedmessages])), labels=[aaa[0] for aaa in tupledeletedmessages],
               rotation=90)
    plt.bar([aaa[0] for aaa in tupledeletedmessages], [aaa[1] for aaa in tupledeletedmessages])
    plt.tight_layout()
    plt.savefig("./graphs/graphdeletedmessages.png")

