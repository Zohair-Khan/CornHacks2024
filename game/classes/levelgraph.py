from levelnode import levelnode
import random

class levelgraph():
    maxwidthmap =	{
                    3 : [1, 2, 3, 2, 1],
                    4 : [1, 2, 3, 4, 3, 2, 1]
                }
    def __init__(self, maxwidth, floorenemies):
        self.nodes = []
        # for i in range(len(self.maxwidthmap[maxwidth])):
        # self.nodes.append([])
        helparr = self.maxwidthmap[maxwidth]
        # print(helparr[0])
        index = 0
        for x in helparr:
            print(x)
            rownodes = []
            for j in range(x):
                newnode = levelnode(random.randint(1, 3))
                
                # self.nodes[index].append(newnode)
                rownodes.append(newnode)
            self.nodes.append(rownodes)
            index+=1

    def printgraph(self):
        print(self.nodes)