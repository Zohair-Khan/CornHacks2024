from player import player
from enemy import enemy
from entity import entity
import random
class fight:

    def attack(attacker: entity, defender: entity):
        # Pull current attacker and defender stats
        attackerstats = attacker.returnStats();
        defenderstats = defender.returnStats();

        #Probably of an attack landing is the probability that an attack lands intersecting the probability that an enemy does not evade 
        attackodds = attackerstats["accuracy"]*(1.0-defenderstats["evasion"])
        #Damage will be the attackers power multiplied by 0 or 1, depending on if the attack lands
        damage = -1.0*attackerstats["power"]*(random.random() <= attackodds)
        #Probability that the given damage becomes critical damage
        if(random.random() <= attackerstats["critrate"]):
            damage = damage*1.5
        print(f"{attacker.getName()} did {-damage} damage to {defender.name}!\n")
        #Update defender HP
        defender.modifyHP(damage)

    def fightcycle(player, enemies):
        # Player and at least one enemy alive
        while(len(enemies) > 0 and player.alive):
            # Player attacks one enemy at random
            fight.attack(player, random.choice(enemies));

            for enemy in enemies:
                if (enemy.getCurrentHP()<=0):
                    print(f"{enemy.name} died!")
                    #Player picks up enemy augments and regenerates some HP upon killing an enemy
                    player.augments+=enemy.augments;
                    player.modifyHP(25-enemy.value)
                    player.updateStats();
                    player.addScore(enemy.value)
                    enemies.remove(enemy)
                else:
                    #Enemies with HP > 0 attack the player
                    fight.attack(enemy, player);
        if (player.alive == False):
            #TO DO // gameOver screen and deeper functionality
            print("Steven has died. So sad!")
            print(player.score)
        else:
            print(f"Steven beat all the enemies on the level! Congratulations! Your score is now: {player.score}")
