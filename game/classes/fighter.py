import pygame
from entity import entity


class Fighter(entity):
    def __init__(self, name, maxhp, power, evasion, accuracy, critrate, x, y, image_path):
        super().__init__(name, maxhp, power, evasion, accuracy, critrate)
        self.score = 0
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.flip = False
        self.attacking = False
        self.attack_type = 0
        self.original_x = x
        self.target_x = None

    def addScore(self, enemyToughness):
        self.score += (15 - enemyToughness) ** 2

    def move(self, screen_width, surface, target):
        SPEED = 5
        dx = 0
        dy = 0

        # get keypress
        key = pygame.key.get_pressed()

        # can only perform move when not currently attacking
        if not self.attacking:
            # movement
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED

            # Update player position
            self.rect.x += dx

            # Handle attack if 'r' key is pressed
            if key[pygame.K_r]:
                self.target_x = target.rect.x  # Set target position to target's x position
                self.original_x = self.rect.x  # Store original position

        # Move towards the target
        if self.target_x is not None:
            if self.rect.x < self.target_x:
                self.rect.x += SPEED
                if self.rect.x >= self.target_x:
                    self.rect.x = self.target_x
                    self.attack(surface, target)
                    self.attacking = True  # Set attacking flag
            elif self.rect.x > self.target_x:
                self.rect.x -= SPEED
                if self.rect.x <= self.target_x:
                    self.rect.x = self.target_x
                    self.attack(surface, target)
                    self.attacking = True  # Set attacking flag

        # Return to original position after attacking
        if self.attacking and self.rect.x == self.target_x:
            if self.rect.x < self.original_x:
                self.rect.x += SPEED
                if self.rect.x >= self.original_x:
                    self.rect.x = self.original_x
                    self.attacking = False  # Reset attacking flag
            elif self.rect.x > self.original_x:
                self.rect.x -= SPEED
                if self.rect.x <= self.original_x:
                    self.rect.x = self.original_x
                    self.attacking = False  # Reset attacking flag

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.maxhp -= 10

    def draw(self, surface):
        player_image = pygame.transform.scale(self.image, (400, 400))
        surface.blit(player_image, self.rect)
