import pygame
import sys
from player import player


def battlefield_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, player):
    # Colors Defining
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (192, 192, 192)
    LIGHT_GREEN = (144, 238, 144)

    # Load background image or draw the battlefield background
    background_image = pygame.image.load(
        "assets/background/battleground.jpg").convert()
    background_image = pygame.transform.scale(
        background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # load player image
    player_image = pygame.image.load("assets/characterImages/Steven.png")
    player_image = pygame.transform.scale(player_image, (150, 150))

    # Game loop for the battlefield screen
    while True:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        # Draw the player on the screen
        screen.blit(player_image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks on any interactive elements
                pass

        # Update the display
        pygame.display.flip()
