import pygame
import sys
from map_screen import map_screen


def start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):

    # Colors Defining
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (192, 192, 192)
    GREEN = (0, 255, 0)
    LIGHT_GREEN = (144, 238, 144)

    # Load background image
    background_image = pygame.image.load(
        "assets/background/battleground.jpg").convert()
    background_image = pygame.transform.scale(
        background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font("freesansbold.ttf", 32)
    small_font = pygame.font.Font("freesansbold.ttf", 20)

    # Button Structure
    button_width = 200
    button_height = 50
    button_spacing = 20

    start_button_rect = pygame.Rect(
        (SCREEN_WIDTH - button_width) // 2, 200, button_width, button_height)  # Center FIrst
    credits_button_rect = pygame.Rect(
        20, SCREEN_HEIGHT - button_height - 20, button_width, button_height)  # Left Bottom

    # Text for buttons
    start_text = font.render("Start", True, BLACK)
    credits_text = font.render("Credits", True, BLACK)

    # Game loop
    while True:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button_rect.collidepoint(event.pos):
                        print("Start button clicked")
                        current_state = map_screen(
                            screen, SCREEN_WIDTH, SCREEN_HEIGHT)

                    elif credits_button_rect.collidepoint(event.pos):
                        print("Credits button clicked")

        # Basic Button drawing
        pygame.draw.rect(screen, GRAY, start_button_rect)
        pygame.draw.rect(screen, GRAY, credits_button_rect)

        # Hover highlight
        if start_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, LIGHT_GREEN, start_button_rect)
        if credits_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, LIGHT_GREEN, credits_button_rect)

        # Writing the text on the buttons
        screen.blit(start_text, (start_button_rect.x + button_width // 2 - start_text.get_width() //
                    2, start_button_rect.y + button_height // 2 - start_text.get_height() // 2))
        screen.blit(credits_text, (credits_button_rect.x + button_width // 2 - credits_text.get_width() //
                    2, credits_button_rect.y + button_height // 2 - credits_text.get_height() // 2))

        pygame.display.flip()
