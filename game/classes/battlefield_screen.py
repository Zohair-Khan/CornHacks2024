import pygame
import sys
from player import player
from fighter import Fighter


def battlefield_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, player):
    # Colors Defining
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (192, 192, 192)
    LIGHT_GREEN = (144, 238, 144)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    # Load background image or draw the battlefield background
    background_image = pygame.image.load(
        "assets/background/battleground.jpg").convert()
    background_image = pygame.transform.scale(
        background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # health bar
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400*ratio, 30))

    # load player image
    player_image = pygame.image.load("assets/characterImages/Steven.png")
    player_image = pygame.transform.scale(player_image, (400, 400))

    # create player
    player_1 = player("Steven", 100, 100, 100, 100, 100)
    fighter_1 = Fighter(100, 200)
    fighter_2 = Fighter(700, 200)

    # Game loop for the battlefield screen
    while True:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        # show health bar
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)

        # Draw the player on the screen
        screen.blit(player_image, (60, 100))
        player_1.move()

        # move fighter
        fighter_1.move(SCREEN_WIDTH, screen, fighter_2)
        # draw fighter
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks on any interactive elements
                pass

        # Update the display
        pygame.display.flip()
