from player import player
from enemy import enemy
from entity import entity
import random


class fight:
    def attack(attacker: entity, defender: entity):
        attackerstats = attacker.returnStats()

        attackodds = attackerstats["accuracy"] * \
            (1.0-defender.returnStats()["evasion"])
        if (random.random() > attackodds):
            return
        else:
            damage = -1.0*attackerstats["power"]
            if (random.random() <= attackerstats["critrate"]):
                damage = damage*1.5
            defender.modifyHP(damage)
