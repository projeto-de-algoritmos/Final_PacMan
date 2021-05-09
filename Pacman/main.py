# Libraries
import pygame
# Functions
from events import treats_event
# Global constants and variables
from config import screen, clock, board, \
                   sprite_list, player, \
                   grape, fruit_list
# Colors
from colors import STANDARD_COLOR

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
