from entity import entity
class enemy(entity):
        def __init__(self, name, maxhp, power, evasion, accuracy, critrate):
            super().__init__(name, maxhp, power, evasion, accuracy, critrate)
