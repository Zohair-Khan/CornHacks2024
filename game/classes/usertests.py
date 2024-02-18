from entity import entity
from player import player
from fight import fight
from augments import augment
from enemy import enemy
from levelnode import levelnode

node1 = levelnode(3)
node2 = levelnode(2)
node1.add_child(node2)
node3 = levelnode(3)
node2.add_child(node3)


enemy1 = enemy("weird al", 11);
enemy2 = enemy("bobby from around the corner", 9);
enemies = [enemy1, enemy2];

steven = player("Even Steven", 60, 20, .4,.6,.3);


fight.fightcycle(steven, enemies);

steven.dispStats();