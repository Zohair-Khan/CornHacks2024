from entity import entity
import pygame


class player(entity):
    def __init__(self, name, maxhp, power, evasion, accuracy, critrate):
        super().__init__(name, maxhp, power, evasion, accuracy, critrate)
        self.image = pygame.image.load("assets/characterImages/Steven.png")
        self.rect = self.image.get_rect()

    def move(self):
        SPEED = 1
        dx = 0
        dy = 0

        # get keypress
        key = pygame.key.get_pressed()

        # movememt
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED

        # update player position
        self.rect.x += dx
        self.rect.y += dy

    def gameOver(self):
        return (self.currenthp <= 0)
