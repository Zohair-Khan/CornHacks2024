import pygame
import sys

pygame.init()

# Colors Defining
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("EVEN Steven Beats ODDS")

# Load background image
background_image = pygame.image.load("backgroundGame.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font("freesansbold.ttf", 32)
small_font = pygame.font.Font("freesansbold.ttf", 20)

# Button Structure
button_width = 200
button_height = 50
button_spacing = 20

start_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, 200, button_width, button_height) #Center FIrst
map_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, 270, button_width, button_height) #Center Second
credits_button_rect = pygame.Rect(20, SCREEN_HEIGHT - button_height - 20, button_width, button_height) #Left Bottom

# Difficulty slider setup
difficulty_slider_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, 450, button_width, button_height)
slider_bar_rect = pygame.Rect(difficulty_slider_rect.x, difficulty_slider_rect.y + difficulty_slider_rect.height // 2 - 2, button_width, 4)
slider_button_radius = 10
slider_button_rect = pygame.Rect(slider_bar_rect.x - slider_button_radius, slider_bar_rect.y + slider_bar_rect.height // 2 - slider_button_radius, slider_button_radius * 2, slider_button_radius * 2)
slider_max_value = 10
slider_value = slider_max_value // 2  #Slider is at Mid difficulty when starting the game

# Text for buttons
start_text = font.render("Start", True, BLACK)
map_text = font.render("Map", True, BLACK)
credits_text = font.render("Credits", True, BLACK)
difficulty_text = font.render("Difficulty", True, BLACK)
easy_text = small_font.render("Easy", True, BLACK)
insane_text = small_font.render("Insane", True, BLACK)

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
                elif map_button_rect.collidepoint(event.pos):
                    print("Map button clicked")
                elif credits_button_rect.collidepoint(event.pos):
                    print("Credits button clicked")
                elif difficulty_slider_rect.collidepoint(event.pos):
                    #Changing the slider value!!
                    slider_value = min(max(0, (event.pos[0] - slider_bar_rect.x) / slider_bar_rect.width * slider_max_value), slider_max_value)

    #Basic Button drawing
    pygame.draw.rect(screen, GRAY, start_button_rect)
    pygame.draw.rect(screen, GRAY, map_button_rect)
    pygame.draw.rect(screen, GRAY, credits_button_rect)
    
    #Hover highlight
    if start_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, LIGHT_GREEN, start_button_rect)
    if map_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, LIGHT_GREEN, map_button_rect)
    if credits_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, LIGHT_GREEN, credits_button_rect)
        
    #Writing the text on the buttons
    screen.blit(start_text, (start_button_rect.x + button_width // 2 - start_text.get_width() // 2, start_button_rect.y + button_height // 2 - start_text.get_height() // 2))
    screen.blit(map_text, (map_button_rect.x + button_width // 2 - map_text.get_width() // 2, map_button_rect.y + button_height // 2 - map_text.get_height() // 2))
    screen.blit(credits_text, (credits_button_rect.x + button_width // 2 - credits_text.get_width() // 2, credits_button_rect.y + button_height // 2 - credits_text.get_height() // 2))

    #The slider
    pygame.draw.rect(screen, BLACK, slider_bar_rect)
    pygame.draw.circle(screen, BLACK, (int(slider_bar_rect.x + slider_value / slider_max_value * slider_bar_rect.width), slider_button_rect.centery), slider_button_radius)
    screen.blit(difficulty_text, (difficulty_slider_rect.x, difficulty_slider_rect.y - 30))
    screen.blit(easy_text, (slider_bar_rect.left, slider_bar_rect.bottom + 5))
    screen.blit(insane_text, (slider_bar_rect.right - insane_text.get_width(), slider_bar_rect.bottom + 5))

    pygame.display.flip()
