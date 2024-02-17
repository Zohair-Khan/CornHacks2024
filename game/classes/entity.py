from augments import augment
class entity:
    augments = []
    currenthp = 99999999
    def __init__(self, name, maxhp, power, evasion, accuracy, critrate):
        self.name = name
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.power = power
        self.evasion = evasion
        self.accuracy = accuracy
        self.critrate = critrate
    def addAugment(self, augment):
        self.augments.append(augment)

    def getBaseStats(self):
        return {"maxhp": self.hp,
                "power": self.power,
                "evasion": self.evasion,
                "accuracy": self.accuracy,
                "critrate": self.critrate}

    def returnStats(self):
        stats = self.getBaseStats()
        for augment in self.augments:
            if(augment.modifier == "multiply"):
                stats[augment.attribute] = stats[augment.attr]*augment.value
            elif (augment.modifier == "add"):
                stats[augment.attribute] = stats[augment.attr]+augment.value
        return stats

    def modifyHP(self, value):
        self.currenthp = self.currenthp+value
        if(self.currenthp < 0):
            self.currenthp = 0

    def gameOver(self):
        return (self.currenthp <= 0)
