import pygame
import sys
from player import player
from fighter import Fighter


def battlefield_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, player):
    # Colors Defining
    WHITE = (255, 255, 255)
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

        if health <= 0:
            print("Enemy died!")

    # create player
    fighter_1 = Fighter("Steven", 100, 100, 100, 100, 100, 50,
                        180, "assets/characterImages/Steven.png")
    fighter_2 = Fighter("Enemy", 100, 100, 100, 100, 100, 600,
                        200, "assets/characterImages/DementedNine.png")

    # Game loop for the battlefield screen
    while True:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        # show health bar
        draw_health_bar(fighter_1.maxhp, 20, 20)
        draw_health_bar(fighter_2.maxhp, 580, 20)

        # move fighter
        fighter_1.move(SCREEN_WIDTH, screen, fighter_2)
        # draw fighter
        fighter_1.draw(screen)

        # draw health bar for fighter_2 if it exists
        if fighter_2 is not None:
            draw_health_bar(fighter_2.maxhp, 580, 20)
            # draw fighter
            fighter_2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks on any interactive elements
                pass

        # Check if fighter_2's health is 0, if so, remove it
        if fighter_2 is not None and fighter_2.maxhp <= 0:
            fighter_2 = None

        # Update the display
        pygame.display.flip()
