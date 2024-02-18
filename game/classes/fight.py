from player import player
from enemy import enemy
from entity import entity
import random


class fight:

    def attack(attacker: entity, defender: entity):
        attackerstats = attacker.returnStats()
        defenderstats = defender.returnStats()
        attackodds = attackerstats["accuracy"]*(1.0-defenderstats["evasion"])
        damage = -1.0*attackerstats["power"]*(random.random() <= attackodds)
        if (random.random() <= attackerstats["critrate"]):
            damage = damage*1.5
        print(f"{attacker.getName()} did {-damage} damage to {defender.name}!\n")
        defender.modifyHP(damage)

    def fightcycle(player, enemies):
        while (len(enemies) > 0 and player.alive):
            fight.attack(player, random.choice(enemies))
            for enemy in enemies:
                if (enemy.getCurrentHP() <= 0):
                    print(f"{enemy.name} died!")
                    enemies.remove(enemy)
                else:
                    fight.attack(enemy, player)
        if (player.alive == False):
            print("Steven has died. So sad!")
