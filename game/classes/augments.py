class augment:

    #Augment class definition
    def __init__(self, name, attribute, modifier, value):
        self.name = name # Flavortext name
        self.attribute = attribute # maxhp, power, accuracy, evasion, or critrate
        self.modifier = modifier #'multiply' or 'add', tells what operation to use
        self.value = value #Value to apply operation with