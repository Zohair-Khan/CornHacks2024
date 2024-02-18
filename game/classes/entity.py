from augments import augment


class entity:
    augments = []
    currenthp = 999
    baseStats = {}
    currentStats = {}

    def __init__(self, name, maxhp, power, evasion, accuracy, critrate):
        self.setName(name)
        self.setMaxHP(maxhp)
        self.setPower(power)
        self.setEvasion(evasion)
        self.setAccuracy(accuracy)
        self.setCritRate(critrate)
        self.baseStats = self.getBaseStats()
        self.currentStats = dict(self.baseStats, currenthp=self.getMaxHP())

    def addAugment(self, augment):
        self.augments.append(augment)

    def getBaseStats(self):
        return {"maxhp": self.getMaxHP(),
                "power": self.getPower(),
                "evasion": self.getEvasion(),
                "accuracy": self.getAccuracy(),
                "critrate": self.getCritRate()}

    def updateStats(self):
        stats = self.getBaseStats()
        for augment in self.augments:
            if (augment.modifier == "multiply"):
                stats[augment.attribute] = stats[augment.attribute]*augment.value
            elif (augment.modifier == "add"):
                stats[augment.attribute] = stats[augment.attribute]+augment.value
        self.currentStats.update(stats)

    def returnStats(self):
        self.updateStats()
        return self.currentStats

    def modifyHP(self, value):
        maxhp = self.returnStats()["maxhp"]
        self.setCurrentHP(self.getCurrentHP()+value)
        if (self.getCurrentHP() <= 0):
            self.gameOver()
        if (self.getCurrentHP > maxhp):
            self.setCurrentHP(maxhp)

    def gameOver(self):
        return (self.getCurrentHP() <= 0)

    # Getters and Setters

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMaxHP(self, maxHP):
        self.maxhp = maxHP

    def getMaxHP(self):
        return self.maxhp

    def setCurrentHP(self, currenthp):
        self.currentStats["currenthp"] = currenthp

    def getCurrentHP(self):
        return self.currentStats["currenthp"]

    def setPower(self, power):
        self.power = power

    def getPower(self):
        return self.power

    def setEvasion(self, evasion):
        self.evasion = evasion

    def getEvasion(self):
        return self.evasion

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    def getAccuracy(self):
        return self.accuracy

    def setCritRate(self, critrate):
        self.critrate = critrate

    def getCritRate(self):
        return self.critrate
