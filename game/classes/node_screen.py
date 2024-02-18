import pygame
import sys
from battlefield_screen import battlefield_screen
from player import player


def node_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (192, 192, 192)
    GREEN = (0, 255, 0)
    LIGHT_GREEN = (144, 238, 144)
    RED = (255, 0, 0)

    # Load background image
    background_image = pygame.image.load(
        "assets/background/battleground.jpg").convert()
    background_image = pygame.transform.scale(
        background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font("freesansbold.ttf", 32)
    small_font = pygame.font.Font("freesansbold.ttf", 20)

    # Variables for map
    map_mode = True
    current_floor = 1
    current_stage = 1
    # Define a list to represent the number of nodes in each row
    nodes_per_row = [1, 2, 3, 2, 1]

    total_nodes = sum(nodes_per_row)
    num_rows = len(nodes_per_row)

    node_width = 50
    node_height = 50
    horizontal_spacing = (SCREEN_WIDTH - node_width) // 10
    vertical_spacing = (SCREEN_HEIGHT - num_rows *
                        node_height) // (num_rows + 20)

    # Generate node positions based on the number of nodes in each row
    node_positions = []
    node_names = []  # List to store node names
    for row, num_nodes in enumerate(nodes_per_row):
        row_width = num_nodes * node_width + \
            (num_nodes - 1) * horizontal_spacing
        start_x = (SCREEN_WIDTH - row_width) // 2
        start_y = (row + 15) * vertical_spacing + row * node_height
        for col in range(num_nodes):
            x = start_x + col * (node_width + horizontal_spacing)
            y = start_y
            node_positions.append((x, y))
            # Generating node names dynamically
            node_names.append(f"{row + 1}{col + 1}")

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

            # Check if a node has already been clicked
            elif event.type == pygame.MOUSEBUTTONDOWN and map_mode and clicked_node is None:
                if event.button == 1:
                    # Check if any node is clicked
                    for i, pos in enumerate(node_positions, start=1):
                        node_rect = pygame.Rect(
                            pos[0] - node_width // 2, pos[1] - node_height // 2, node_width, node_height)

                        if node_rect.collidepoint(event.pos):
                            clicked_node = i  # Record the clicked node
                            break  # No need to check other nodes if one is already clicked

        if map_mode:

            floor_label = font.render(f"Stage {current_floor}", True, BLACK)
            screen.blit(floor_label, (480 -
                        floor_label.get_width() // 2, 70))

            # Draw lines between adjacent nodes
            for row in range(num_rows - 1):
                for col in range(nodes_per_row[row]):
                    # Calculate the index of the current node
                    current_node_index = sum(nodes_per_row[:row]) + col
                    current_node_pos = node_positions[current_node_index]

                    # Draw lines to nodes in the row below
                    for col_below in range(nodes_per_row[row + 1]):
                        below_node_index = sum(
                            nodes_per_row[:row + 1]) + col_below
                        below_node_pos = node_positions[below_node_index]

                        # Draw a line between the current node and the node below it
                        pygame.draw.line(
                            screen, BLACK, current_node_pos, below_node_pos)

            # Draw nodes and make them clickable
            for i, pos in enumerate(node_positions, start=1):

                node_rect = pygame.Rect(
                    pos[0] - node_width // 2, pos[1] - node_height // 2, node_width, node_height)

                # Check if node is clicked
                if clicked_node == i:
                    pygame.draw.rect(screen, LIGHT_GREEN, node_rect)
                    print(f"Clicked node {node_names[i - 1]}")
                    # Check if the clicked node is in the first row
                    if i <= nodes_per_row[0]:
                        # Transition to battlefield screen
                        current_screen = battlefield_screen(
                            screen, SCREEN_WIDTH, SCREEN_HEIGHT, player)
                # Check if mouse is over the node
                elif node_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, LIGHT_GREEN, node_rect)

                    hovered_node = i  # Record the hovered node
                else:
                    pygame.draw.rect(screen, GRAY, node_rect)

                # Write node number on the nodes
                node_number_text = small_font.render(
                    node_names[i - 1], True, BLACK)
                screen.blit(node_number_text, (pos[0] - node_number_text.get_width(
                ) // 2, pos[1] - node_number_text.get_height() // 2))

        pygame.display.flip()
