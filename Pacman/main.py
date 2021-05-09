# Libraries
import pygame
import os
# Functions
from events import treats_event
# Global constants and variables
from config import screen, clock, board, \
                   sprite_list, player, \
                   fruit_list
# Colors
from colors import STANDARD_COLOR, WALL, BLACK

MENU_CHOICE = 1

def main_game() -> int:
    """ The game loop
            Parameters:
                None
            Returns:
                int: 0 to close the program
    """
    board.draw_grid(screen)
    board.maze_prim(1, 1, screen)
    board.store_maze(screen)
    board.free_space()

    for i in range (len(fruit_list)):
        fruit_list[i].set_position()

    done = False
    while not done:
        # Frame rate
        clock.tick(60)
        # Fill the screen
        screen.fill(STANDARD_COLOR)
        # Draw and update sprites
        sprite_list.draw(screen)
        sprite_list.update()
        # Draw the maze
        board.draw_maze(screen)
        # Update screen
        pygame.display.flip()
        # Treats player interaction
        for event in pygame.event.get():
            done = treats_event(event)
    return 0

def main_menu():
    """ The menu loop
            Parameters:
                None
            Returns:
                int: 0 to close the program
    """
    button_start = pygame.Rect(450, 400, 700, 200)
    done = False
    x = 0
    y = 0

    menuimg = pygame.image.load(os.path.join('images', 'menu.png')).convert()
    menurect = menuimg.get_rect()
    while not done:
        # Frame rate
        clock.tick(60)
        # Fill the screen
        screen.fill(WALL)
        screen.blit(menuimg, menurect)
        # Update screen
        pygame.display.flip()
        # Events
        if button_start.collidepoint(x, y) and click == True:
            return 2

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if event.button == 1:
                    click = True
    return 0

while MENU_CHOICE != 0:
    if MENU_CHOICE == 1:
        MENU_CHOICE = main_menu()
    elif MENU_CHOICE == 2:
        MENU_CHOICE = main_game()
