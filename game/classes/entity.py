from augments import augment
class entity:
    augments = []
    def __init__(self, name, hp, power, evasion, accuracy, critrate):
        self.name = name
        self.hp = hp
        self.power = power
        self.evasion = evasion
        self.accuracy = accuracy
        self.critrate = critrate
    def addAugment(self, augment):
        self.augments.append(augment)


