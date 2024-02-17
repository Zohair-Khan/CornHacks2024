import pygame


def start_screen(screen, MAP_SCREEN, START_SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT):
    font = pygame.font.SysFont('arial', 40)
    title = font.render("Click Start to Begin", True, (255, 255, 255))

    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width() /
                2, SCREEN_HEIGHT/2 - title.get_height()/2))
    screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width() /
                2, SCREEN_HEIGHT/2 + start_button.get_height()/2))
    pygame.display.update()

    # Detect mouse click events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos):
                return MAP_SCREEN
    return START_SCREEN
