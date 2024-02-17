#GO TO LINE 88, I THINK THE PROBLEM IS AFTER THAT   

import pygame
import sys

pygame.init()

# Colors Defining
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
RED = (255, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("EVEN Steven Beats ODDS")
background_image = pygame.image.load("backgroundGame.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font("freesansbold.ttf", 32)
small_font = pygame.font.Font("freesansbold.ttf", 20)

#Button Structure
button_width = 200
button_height = 50
button_spacing = 20

start_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, 200, button_width, button_height) #Center First
map_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, 270, button_width, button_height) #Center Second
credits_button_rect = pygame.Rect(20, SCREEN_HEIGHT - button_height - 20, button_width, button_height) #Left Bottom

#Text for buttons
start_text = font.render("Start", True, BLACK)
map_text = font.render("Map", True, BLACK)
credits_text = font.render("Credits", True, BLACK)
difficulty_text = font.render("Difficulty", True, BLACK)
easy_text = small_font.render("Easy", True, BLACK)
insane_text = small_font.render("Insane", True, BLACK)

# Variables for map
map_mode = False
current_floor = 1
current_stage = 1

# Game loop
while True:
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not map_mode:
            if event.button == 1:
                if start_button_rect.collidepoint(event.pos):
                    print("Start button clicked")
                elif map_button_rect.collidepoint(event.pos):
                    print("Map button clicked")
                    map_mode = True
                elif credits_button_rect.collidepoint(event.pos):
                    print("Credits button clicked")

    if map_mode:
        #Map plotting
        pygame.draw.rect(screen, WHITE, (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100))
        pygame.draw.rect(screen, BLACK, (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100), 2)
        floor_label = font.render(f"Floor {current_floor}", True, BLACK)
        screen.blit(floor_label, (500 - floor_label.get_width() // 2, 70))
    
        #Node defining
        node_positions = [
            (SCREEN_WIDTH // 2, 100),  # Top node
            (SCREEN_WIDTH // 2 - 150, 250),  # Left node
            (SCREEN_WIDTH // 2 + 150, 250),  # Right node
            (SCREEN_WIDTH // 2, 400),  # Center (boss) node
        ]
    
        # to track if a node has been clicked or not
        node_clicked = [False] * len(node_positions)
    
        # Draw nodes and make them clickable
        for i, pos in enumerate(node_positions, start=1):
            node_rect = pygame.Rect(pos[0] - 25, pos[1] - 25, 50, 50)
            pygame.draw.polygon(screen, GRAY, [(pos[0], pos[1] - 20), (pos[0] + 20, pos[1]), (pos[0], pos[1] + 20), (pos[0] - 20, pos[1])])
            pygame.draw.polygon(screen, BLACK, [(pos[0], pos[1] - 20), (pos[0] + 20, pos[1]), (pos[0], pos[1] + 20), (pos[0] - 20, pos[1])], 2)
            
            # Check if node is clicked
            if node_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, LIGHT_GREEN, node_rect)
                if pygame.mouse.get_pressed()[0] and not node_clicked[i - 1]:  # Check left mouse button click
                    node_clicked[i - 1] = True
                    print(f"Clicked node {i}")
            else:
                pygame.draw.rect(screen, GRAY, node_rect)
    
            #write node number on the nodes
            node_number_text = small_font.render(str(i), True, BLACK)
            screen.blit(node_number_text, (pos[0] - node_number_text.get_width() // 2, pos[1] - node_number_text.get_height() // 2))
    
    else:
        # Basic Button drawing
        pygame.draw.rect(screen, GRAY, start_button_rect)
        pygame.draw.rect(screen, GRAY, map_button_rect)
        pygame.draw.rect(screen, GRAY, credits_button_rect)

        # Hover highlight
        if start_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, LIGHT_GREEN, start_button_rect)
        if map_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, LIGHT_GREEN, map_button_rect)
        if credits_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, LIGHT_GREEN, credits_button_rect)

        # Writing the text on the buttons
        screen.blit(start_text, (start_button_rect.x + button_width // 2 - start_text.get_width() // 2, start_button_rect.y + button_height // 2 - start_text.get_height() // 2))
        screen.blit(map_text, (map_button_rect.x + button_width // 2 - map_text.get_width() // 2, map_button_rect.y + button_height // 2 - map_text.get_height() // 2))
        screen.blit(credits_text, (credits_button_rect.x + button_width // 2 - credits_text.get_width() // 2, credits_button_rect.y + button_height // 2 - credits_text.get_height() // 2))

    pygame.display.flip()
