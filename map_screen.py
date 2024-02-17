import pygame
import sys


def map_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    # Colors Defining
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (192, 192, 192)
    LIGHT_GREEN = (144, 238, 144)

    # Load background image
    map_image = pygame.image.load(
        "assets/background/map_bg.png").convert()
    map_image = pygame.transform.scale(
        map_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define any buttons or interactive elements specific to the map screen

    # Game loop for the map screen
    while True:

        # Render any elements specific to the map screen
        # This may include the map background, level buttons, etc.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks on any interactive elements
                # For example, if a level button is clicked, you may transition to the battlefield screen
                pass  # Replace this with your logic

        # Update the display
        pygame.display.flip()
