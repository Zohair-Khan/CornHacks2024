from entity import entity
from augments import augment
import random

class enemy(entity):
		#Defines all possible augments held by an enemy of a given value
		enemyAugments =	{   11: [   augment("Inferior Augment of Additive HP", "maxhp","add",2)                , 
							        augment("Inferior Augment of Multiplicative HP","maxhp","multiply",1.05)   ,
							        augment("Inferior Augment of Additive Power","power","add",5)              , 
							        augment("Inferior Augment of Multiplicative Power","power","multiply",1.15),
							        augment("Inferior Augment of Critical Chance","critrate","add",.005)       ,
							        augment("Inferior Augment of Evasion","evasion","add",.01)                 , 
							        augment("Inferior Augment of Accuracy","accuracy","add",.01)               ],
							9 : [   augment("Petty Augment of Additive HP", "maxhp","add",4)                   , 
							        augment("Petty Augment of Multiplicative HP","maxhp","multiply",1.075)     ,
							        augment("Petty Augment of Additive Power","power","add",10)                , 
							        augment("Petty Augment of Multiplicative Power","power","multiply",1.2)    ,
							        augment("Petty Augment of Critical Chance","critrate","add",.01)           ,
							        augment("Petty Augment of Evasion","evasion","add",.015)                   , 
							        augment("Petty Augment of Accuracy","accuracy","add",.015)                 ],
							7 : [   augment("Lesser Augment of Additive HP", "maxhp","add",10)                 , 
							        augment("Lesser Augment of Multiplicative HP","maxhp","multiply",1.125)    ,
							        augment("Lesser Augment of Additive Power","power","add",15)               , 
							        augment("Lesser Augment of Multiplicative Power","power","multiply",1.25)  ,
							        augment("Lesser Augment of Critical Chance","critrate","add",.015)         ,
							        augment("Lesser Augment of Evasion","evasion","add",.02)                   , 
							        augment("Lesser Augment of Accuracy","accuracy","add",.02)                 ],
							5 : [   augment("Greater Augment of Additive HP", "maxhp","add",20)                , 
							        augment("Greater Augment of Multiplicative HP","maxhp","multiply",1.175)   ,
							        augment("Greater Augment of Additive Power","power","add",25)              , 
							        augment("Greater Augment of Multiplicative Power","power","multiply",1.3)  ,
							        augment("Greater Augment of Critical Chance","critrate","add",.02)         ,
							        augment("Greater Augment of Evasion","evasion","add",.025)                 , 
								    augment("Greater Augment of Accuracy","accuracy","add",.025)               ],
							3 : [   augment("Superior Augment of Additive HP", "maxhp","add",35)               , 
							        augment("Superior Augment of Multiplicative HP","maxhp","multiply",1.25)   ,
							        augment("Superior Augment of Additive Power","power","add",50)             , 
							        augment("Superior Augment of Multiplicative Power","power","multiply",1.4) ,
							        augment("Superior Augment of Critical Chance","critrate","add",.03)        ,
							        augment("Superior Augment of Evasion","evasion","add",.04)                 , 
							        augment("Superior Augment of Accuracy","accuracy","add",.04)               ],
							1 :  [  augment("Godly Augment of Additive HP", "maxhp", "add",60)                 ,
			 						augment("Godly Augment of Multiplicative HP", "maxhp",  "multiply", 1.35)  ,
									augment("Godly Augment of Additive Power", "power", "add",80)              ,
									augment("Godly Augment of Multiplicative Power","power", "multiply",1.55)  ,
									augment("Godly Augment of Critical Chance","critrate", "add",.08)          ,
									augment("Godly Augment of Evasion", "evasion", "add",.09)                  ,
									augment("Godly Augment of Accuracy", "accuracy", "add",.09)                ]}

		#Defines all base stats of enemies of a given value
		enemyBaseStats = {11: {"name": "Useless Eleven", "maxhp": 20, "power": 10, "evasion": .30, "accuracy": .60, "critrate": .10}  , 
						  9 : {"name": "Nefarious Nine" , "maxhp": 35, "power": 32, "evasion": .36, "accuracy": .68, "critrate": .20} ,
						  7 : {"name": "Savage Seven" , "maxhp": 40, "power": 46, "evasion": .42, "accuracy": .76, "critrate": .40}   ,
						  5 : {"name": "Fearsome Five" , "maxhp": 90, "power": 46, "evasion": .42, "accuracy": .80, "critrate": .25}  ,
						  3 : {"name": "Trickster Three" , "maxhp": 80, "power": 55, "evasion": .65, "accuracy": .92, "critrate": .30},
						  1 : {"name": "One" , "maxhp": 100, "power": 90, "evasion": .3, "accuracy": 1.0, "critrate": .40}            }

		def __init__(self, value):
			super().__init__(self.enemyBaseStats[value]["name"], self.enemyBaseStats[value]["maxhp"],self.enemyBaseStats[value]["power"], self.enemyBaseStats[value]["evasion"], self.enemyBaseStats[value]["accuracy"], self.enemyBaseStats[value]["critrate"])
			self.addAugment(random.choice(self.enemyAugments[value]))
			self.value = value

		def bossify(self):
			#Bosses draw an additional augment!
			self.addAugment(random.choice(self.enemyAugments[self.value]))