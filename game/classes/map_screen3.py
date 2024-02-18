import pygame
import sys
from node_screen import node_screen
from player import player


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

    # Define level 3 button
    level3_button_img = pygame.image.load("assets/icon/levelicon.png")
    button_width, button_height = 150, 100
    level3_button_img = pygame.transform.scale(
        level3_button_img, (button_width, button_height))
    level3_button_img_hover = pygame.transform.scale(
        level3_button_img, (button_width*0.9, button_height*0.9))

    # Define level 3 button
    level3_button_rect = level3_button_img.get_rect(bottomleft=(330, 430))

    # track current level
    current_level = None

    # Game loop for the map screen
    while True:
        screen.fill(WHITE)
        screen.blit(map_image, (0, 0))

        # Check if the mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        if level3_button_rect.collidepoint(mouse_pos):
            screen.blit(level3_button_img_hover, level3_button_rect)
        else:
            screen.blit(level3_button_img, level3_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if level3_button_rect.collidepoint(event.pos):
                    current_level = 3
                    current_state = node_screen(
                        screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Update the display
        pygame.display.flip()
