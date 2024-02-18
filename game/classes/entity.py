from augments import augment
class entity:
    def __init__(self, name, maxhp, power, evasion, accuracy, critrate):
        # set all attributes
        self.setName(name)
        self.setMaxHP(maxhp)
        self.setPower(power)
        self.setEvasion(evasion)
        self.setAccuracy(accuracy)
        self.setCritRate(critrate)
        # initialize stats dictionaries and augments list
        self.baseStats = self.getBaseStats();
        self.currentStats = dict(self.baseStats, currenthp = self.getMaxHP());
        self.augments = [];
        self.alive = True;

    def addAugment(self, augment):
        self.augments.append(augment)
        self.updateStats()

    def getAugments(self):
        # Print out a list of augment names
        str = ""
        for augment in self.augments:
            str+=augment.name;
            str+="\n";
        return str

    def getBaseStats(self):
        return  {"maxhp"   : self.getMaxHP()    ,
                 "power"   : self.getPower()    ,
                 "evasion" : self.getEvasion()  ,
                 "accuracy": self.getAccuracy() ,
                 "critrate": self.getCritRate()};

    def updateStats(self):
        stats = self.getBaseStats()
        stats.update({"currenthp": self.getCurrentHP()});
        for augment in self.augments:
            if(augment.modifier == "multiply"):
                    stats[augment.attribute]*=augment.value
            elif(augment.modifier == "add"):
                    stats[augment.attribute]+=augment.value
            if(augment.attribute == "maxhp"):
                # adjusts currenthp with augments without exceeding maxhp
                stats["currenthp"] = min(stats["maxhp"],stats["currenthp"]*augment.value if augment.modifier == "multiply" else stats["currenthp"]+augment.value)
        self.currentStats.update(stats);

    def returnStats(self):
        #updates stats and returns current stats
        self.updateStats();
        return self.currentStats;

    def modifyHP(self, value):
        # ensure modified hp does not exceed maxhp and triggers game over event if health drops to 0 or less
        maxhp = self.returnStats()["maxhp"]
        self.setCurrentHP(self.getCurrentHP()+value)
        if(self.getCurrentHP() <= 0):
            self.setCurrentHP(0);
            self.gameOver();
        if(self.getCurrentHP() > maxhp):
            self.setCurrentHP(maxhp)

    def gameOver(self):
        self.alive = False;

    def dispStats(self):
        # Debug view of stats
        print(f"Name: {self.name}")
        print(f"HP: {self.getCurrentHP()}/"+str(self.currentStats["maxhp"]));
        print(f"Power: "+ str(self.currentStats["power"]))
        print(f"Critical Hit Chance: " + str(self.currentStats["critrate"]))
        print(f"Accuracy: " + str(self.currentStats["accuracy"]))
        print(f"Evasion Chance: "+ str(self.currentStats["evasion"]));
        print("Augments:\n"+self.getAugments());


    #Getters and Setters
    def setName(self, name):
        self.name = name;
    def getName(self):
        return self.name;

    def setMaxHP(self, maxHP):
        self.maxhp = maxHP;
    def getMaxHP(self):
        return self.maxhp;

    def setCurrentHP(self, currenthp):
        self.currentStats["currenthp"] = currenthp;
    def getCurrentHP(self):
        return self.currentStats["currenthp"]

    def setPower(self, power):
        self.power = power;
    def getPower(self):
        return self.power;

    def setEvasion(self, evasion):
        self.evasion = evasion;
    def getEvasion(self):
        return self.evasion;    

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy;
    def getAccuracy(self):
        return self.accuracy; 

    def setCritRate(self, critrate):
        self.critrate = critrate;
    def getCritRate(self):
        return self.critrate;
