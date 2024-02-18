import pygame


class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 100, 280))
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def move(self, screen_width, surface, target):
        SPEED = 1
        dx = 0
        dy = 0

        # get keypress
        key = pygame.key.get_pressed()

        # can only perform move when not currently attacking
        if self.attacking == False:
            # movememt
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED

            # attack
            if key[pygame.K_r]:
                self.attack(surface, target)
                self.attacl_type = 1

            # ensure player stays on screen
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > screen_width:
                dx = screen_width - self.rect.right

            # update player position
            self.rect.x += dx
            self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (255, 0, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)
