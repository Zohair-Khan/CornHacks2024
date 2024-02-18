from levelnode import levelnode
import random

class levelgraph():
    maxwidthmap =	{
                    2 : [1, 2, 1],
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
            # print(x)
            rownodes = []
            for j in range(x):
                newnode = levelnode(random.randint(1, 3))
                
                # self.nodes[index].append(newnode)
                rownodes.append(newnode)
            self.nodes.append(rownodes)
            index+=1

        # setting children
        rowindex = 0
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[rowindex])):
                # print(i, j)
                # if(len(self.nodes[rowindex])<maxwidth):
                if(i<(len(self.nodes)/2.0)-1):
                    # print("tophalf")
                    # check node below
                    if(i+1<len(self.nodes)):
                        # print(f"adding {i+1}, {j}")
                        self.nodes[i][j].add_child(self.nodes[i+1][j])
                        
                    # check node on bottom right
                    if(i+1<len(self.nodes)):
                        # print(f"adding {i+1}, {j+1}")
                        self.nodes[i][j].add_child(self.nodes[i+1][j+1])
                        
                else:
                    #check node below
                    if(i+1<len(self.nodes) and j<len(self.nodes[rowindex+1])):
                        # print(f"adding {i+1}, {j}")
                        self.nodes[i][j].add_child(self.nodes[i+1][j])
                        
                    # check node bottom left
                    if(i+1<len(self.nodes) and j-1>=0):
                        # print(f"adding {i+1}, {j-1}")
                        self.nodes[i][j].add_child(self.nodes[i+1][j-1])
                        
            rowindex+=1


    def printgraph(self):
        print(self.nodes)