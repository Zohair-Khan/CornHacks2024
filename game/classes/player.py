from entity import entity


class player(entity):
    def __init__(self, name, maxhp, power, evasion, accuracy, critrate):
        super().__init__(name, maxhp, power, evasion, accuracy, critrate)

    def gameOver(self):
        return (self.currenthp <= 0)
