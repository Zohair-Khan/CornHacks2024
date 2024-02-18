import pygame
import sys

pygame.init()

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
background_image = pygame.transform.scale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font("freesansbold.ttf", 32)
small_font = pygame.font.Font("freesansbold.ttf", 20)

# Button Structure
button_width = 200
button_height = 50
button_spacing = 20

start_button_rect = pygame.Rect(
    (SCREEN_WIDTH - button_width) // 2, 200, button_width, button_height)  # Center First
map_button_rect = pygame.Rect(
    (SCREEN_WIDTH - button_width) // 2, 270, button_width, button_height)  # Center Second
credits_button_rect = pygame.Rect(
    20, SCREEN_HEIGHT - button_height - 20, button_width, button_height)  # Left Bottom

# Text for buttons
start_text = font.render("Start", True, BLACK)
map_text = font.render("Map", True, BLACK)
credits_text = font.render("Credits", True, BLACK)

# Variables for map
map_mode = False
current_floor = 3
current_stage = 3
# Define a list to represent the number of nodes in each row
nodes_per_row = [1, 2, 3, 4, 3, 2, 1]

total_nodes = sum(nodes_per_row)
num_rows = len(nodes_per_row)

node_width = 50
node_height = 50
horizontal_spacing = (SCREEN_WIDTH - node_width) // 10
vertical_spacing = (SCREEN_HEIGHT - num_rows * node_height) // (num_rows + 20)

# Generate node positions based on the number of nodes in each row
node_positions = []
node_names = []  # List to store node names
for row, num_nodes in enumerate(nodes_per_row):
    row_width = num_nodes * node_width + (num_nodes - 1) * horizontal_spacing
    start_x = (SCREEN_WIDTH - row_width) // 2
    start_y = (row + 15) * vertical_spacing + row * node_height
    for col in range(num_nodes):
        x = start_x + col * (node_width + horizontal_spacing)
        y = start_y
        node_positions.append((x, y))
        node_names.append(f"{row + 1}{col + 1}")  # Generating node names dynamically

# Game loop
while True:
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))

    clicked_node = None  # Variable to track the clicked node
    hovered_node = None  # Variable to track the hovered node

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

        elif event.type == pygame.MOUSEBUTTONDOWN and map_mode and clicked_node is None:  # Check if a node has already been clicked
            if event.button == 1:
                # Check if any node is clicked
                for i, pos in enumerate(node_positions, start=1):
                    node_rect = pygame.Rect(pos[0] - node_width // 2, pos[1] - node_height // 2, node_width, node_height)

                    if node_rect.collidepoint(event.pos):
                        clicked_node = i  # Record the clicked node
                        break  # No need to check other nodes if one is already clicked

    if map_mode:

        # Map plotting
        pygame.draw.rect(screen, WHITE, (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100))
        pygame.draw.rect(screen, BLACK, (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100), 2)

        floor_label = font.render(f"Floor {current_floor}", True, BLACK)
        screen.blit(floor_label, (500 - floor_label.get_width() // 2, 70))

        # Draw nodes and make them clickable
        for i, pos in enumerate(node_positions, start=1):

            node_rect = pygame.Rect(pos[0] - node_width // 2, pos[1] - node_height // 2, node_width, node_height)

            # Check if node is clicked
            if clicked_node == i:
                pygame.draw.rect(screen, LIGHT_GREEN, node_rect)
                print(f"Clicked node {node_names[i - 1]}")
            elif node_rect.collidepoint(pygame.mouse.get_pos()):  # Check if mouse is over the node
                pygame.draw.rect(screen, LIGHT_GREEN, node_rect)

                hovered_node = i  # Record the hovered node
            else:
                pygame.draw.rect(screen, GRAY, node_rect)

            # Write node number on the nodes
            node_number_text = small_font.render(node_names[i - 1], True, BLACK)
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
        screen.blit(start_text, (start_button_rect.x + button_width // 2 - start_text.get_width() //
                    2, start_button_rect.y + button_height // 2 - start_text.get_height() // 2))
        screen.blit(map_text, (map_button_rect.x + button_width // 2 - map_text.get_width() //
                    2, map_button_rect.y + button_height // 2 - map_text.get_height() // 2))
        screen.blit(credits_text, (credits_button_rect.x + button_width // 2 - credits_text.get_width() //
                    2, credits_button_rect.y + button_height // 2 - credits_text.get_height() // 2))

    pygame.display.flip()
