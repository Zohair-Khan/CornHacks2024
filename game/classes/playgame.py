from entity import entity
from player import player
from fight import fight
from augments import augment
from enemy import enemy
from levelnode import levelnode
from levelgraph import levelgraph
import random

steven = player("Even Steven", 80, 200, .4,.65,.3)
floor1enemies = (11, 9, 7)
floor2enemies = (9, 7, 5)
floor3enemies = (7, 5, 3)

# going through first floor
floor1 = levelgraph(3, floor1enemies)
print(len(floor1.nodes))
currentnode = floor1.nodes[0][0]
traversaldepth = 0
while traversaldepth < len(floor1.nodes)-1:
    print(f"{traversaldepth}, {len(floor1.nodes)-1}")
    if(traversaldepth != len(floor1.nodes)-1):
        currentnode.onNodeTriggered(steven, floor1enemies)
        print(f"\nBeat Room {traversaldepth+1}!\n")
    traversaldepth +=1
    if(traversaldepth < len(floor1.nodes)-1):
        print("Choose the next room to go to:")
        index = 1
        for child in currentnode.children:
            print(f"{index}: Difficulty: {child.difficulty}")
            index+=1
        
        choice = input("Room: ")
        currentnode = currentnode.children[int(choice)-1]
        

currentnode.onNodeTriggered(steven, [5])

