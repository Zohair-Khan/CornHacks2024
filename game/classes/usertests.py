from entity import entity
from player import player
from fight import fight
from augments import augment
from enemy import enemy
from levelnode import levelnode
from levelgraph import levelgraph
import random

floorenemies = [11, 9, 7]
steven = player("Even Steven", 1000, 20, .4,.6,.3);

floorgraph = levelgraph(3, floorenemies)
floorgraph.printgraph()



# node1 = levelnode(random.randint(1, 3))
# node2 = levelnode(random.randint(1, 3))
# node1.add_child(node2)
# node3 = levelnode(random.randint(1, 3))
# node2.add_child(node3)

# print("entering Node 1!")
# node1.onNodeTriggered(steven, floorenemies)
# print("entering Node 2!")
# node2.onNodeTriggered(steven, floorenemies)
# print("entering Node 3!")
# node3.onNodeTriggered(steven, floorenemies)

# enemy1 = enemy("weird al", 11);
# enemy2 = enemy("bobby from around the corner", 9);
# enemies = [enemy1, enemy2];

# steven = player("Even Steven", 60, 20, .4,.6,.3);


# fight.fightcycle(steven, enemies);

# steven.dispStats();