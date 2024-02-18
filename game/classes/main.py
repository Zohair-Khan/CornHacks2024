from start_screen import start_screen
from map_screen import map_screen
from battlefield_screen import battlefield_screen
from player import player
import pygame
import sys

# define game states
START_SCREEN = 0
MAP_SCREEN = 1
BATTLE_SCREEN = 2

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("EVEN Steven Beats ODDS")

# load player image
player_image = pygame.image.load("assets/characterImages/Steven.png")

current_screen = START_SCREEN

# game loop
run = True
while run:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if current_screen == START_SCREEN:
            current_screen = start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif current_screen == MAP_SCREEN:
            current_screen = map_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif current_screen == BATTLE_SCREEN:
            current_screen = battlefield_screen(
                screen, SCREEN_WIDTH, SCREEN_HEIGHT, player_image)

    pygame.display.flip()  # Update display

# exit pygame
pygame.quit()
sys.exit()
