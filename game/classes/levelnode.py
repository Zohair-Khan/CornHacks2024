from entity import entity
from player import player
from fight import fight
from augments import augment
from enemy import enemy
import random

class levelnode:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.children = []

    def onNodeTriggered(self, player, floorenemies):
        enemies = []
        for i in range(self.difficulty):
            newEnemy = enemy(random.choice(floorenemies))
            enemies.append(newEnemy)
        fight.fightcycle(player, enemies)
        player.dispStats()
        

    def add_child(self, child):
        self.children.append(child)