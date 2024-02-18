from entity import entity
import pygame


class player(entity):
    def __init__(self, name, maxhp, power, evasion, accuracy, critrate, image):
        super().__init__(name, maxhp, power, evasion, accuracy, critrate)
        self.image = image

    def gameOver(self):
        return (self.currenthp <= 0)
