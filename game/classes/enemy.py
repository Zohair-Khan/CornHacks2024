from entity import entity
from augments import augment
import random

class enemy(entity):
		enemyAugments =	{11: [augment("Inferior Augment of Additive HP", "maxhp","add",2)                , 
							        augment("Inferior Augment of Multiplicative HP","maxhp","multiply",1.05)   ,
							        augment("Inferior Augment of Additive Power","power","add",5)              , 
							        augment("Inferior Augment of Multiplicative Power","power","multiply",1.15),
							        augment("Inferior Augment of Critical Chance","critrate","add",.005)       ,
							        augment("Inferior Augment of Evasion","evasion","add",.01)                 , 
							        augment("Inferior Augment of Accuracy","accuracy","add",.01)               ],
							9 : [ augment("Petty Augment of Additive HP", "maxhp","add",4)                   , 
							        augment("Petty Augment of Multiplicative HP","maxhp","multiply",1.075)     ,
							        augment("Petty Augment of Additive Power","power","add",10)                , 
							        augment("Petty Augment of Multiplicative Power","power","multiply",1.2)    ,
							        augment("Petty Augment of Critical Chance","critrate","add",.01)           ,
							        augment("Petty Augment of Evasion","evasion","add",.015)                   , 
							        augment("Petty Augment of Accuracy","accuracy","add",.015)                 ],
							7 : [ augment("Lesser Augment of Additive HP", "maxhp","add",10)                 , 
							        augment("Lesser Augment of Multiplicative HP","maxhp","multiply",1.125)    ,
							        augment("Lesser Augment of Additive Power","power","add",15)               , 
							        augment("Lesser Augment of Multiplicative Power","power","multiply",1.25)  ,
							        augment("Lesser Augment of Critical Chance","critrate","add",.015)         ,
							        augment("Lesser Augment of Evasion","evasion","add",.02)                   , 
							        augment("Lesser Augment of Accuracy","accuracy","add",.02)                 ],
							5 : [ augment("Greater Augment of Additive HP", "maxhp","add",20)                , 
							        augment("Greater Augment of Multiplicative HP","maxhp","multiply",1.175)   ,
							        augment("Greater Augment of Additive Power","power","add",25)              , 
							        augment("Greater Augment of Multiplicative Power","power","multiply",1.3)  ,
							        augment("Greater Augment of Critical Chance","critrate","add",.02)         ,
							        augment("Greater Augment of Evasion","evasion","add",.025)                 , 
								augment("Greater Augment of Accuracy","accuracy","add",.025)               ],
							3 : [ augment("Superior Augment of Additive HP", "maxhp","add",40)               , 
							        augment("Superior Augment of Multiplicative HP","maxhp","multiply",1.25)   ,
							        augment("Superior Augment of Additive Power","power","add",50)             , 
							        augment("Superior Augment of Multiplicative Power","power","multiply",1.4) ,
							        augment("Superior Augment of Critical Chance","critrate","add",.03)        ,
							        augment("Superior Augment of Evasion","evasion","add",.04)                 , 
							        augment("Superior Augment of Accuracy","accuracy","add",.04)               ]}

		enemyBaseStats = {11: {"name": "11placeholder", "maxhp": 20, "power": 10, "evasion": .30, "accuracy": .60, "critrate": .10}, 
						  9 : {"name": "9placeholder", "maxhp": 35, "power": 18, "evasion": .36, "accuracy": .68, "critrate": .15},
						  7 : {"name": "7placeholder", "maxhp": 50, "power": 30, "evasion": .42, "accuracy": .76, "critrate": .20},
						  5 : {"name": "5placeholder", "maxhp": 65, "power": 46, "evasion": .48, "accuracy": .84, "critrate": .25},
						  3 : {"name": "3placeholder", "maxhp": 80, "power": 66, "evasion": .54, "accuracy": .92, "critrate": .30},
						  1 : {"name": "1placeholder", "maxhp": 100, "power": 90, "evasion": .3, "accuracy": 1.0, "critrate": .40},}

		def __init__(self, value):
			super().__init__(self.enemyBaseStats[value]["name"], self.enemyBaseStats[value]["maxhp"],self.enemyBaseStats[value]["power"], self.enemyBaseStats[value]["evasion"], self.enemyBaseStats[value]["accuracy"], self.enemyBaseStats[value]["critrate"])
			self.addAugment(random.choice(self.enemyAugments[value]))
			self.value = value
