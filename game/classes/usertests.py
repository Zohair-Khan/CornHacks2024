from entity import entity
from player import player
from fight import fight
from augments import augment
from enemy import enemy
from levelnode import levelnode
import random

floorenemies = [11, 9, 7]
steven = player("Even Steven", 80, 30, .4,.65,.325);

node1 = levelnode(random.randint(1, 3))
node2 = levelnode(random.randint(1, 3))
node1.add_child(node2)
node3 = levelnode(random.randint(1, 3))
node2.add_child(node3)

node1.onNodeTriggered(steven, floorenemies)
node2.onNodeTriggered(steven, floorenemies)
node3.onNodeTriggered(steven, floorenemies)
