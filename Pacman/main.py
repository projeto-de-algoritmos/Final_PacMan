# Libraries
import pygame
# Functions
from events import treats_event
# Global constants and variables
from config import screen, clock, board, sprite_list, player, ghost
# Colors
from colors import STANDARD_COLOR

board.draw_grid(screen)
board.maze_prim(1, 1, screen)
board.store_maze(screen)

done = False
while not done:
    # Frame rate
    clock.tick(60)
    # Fill the screen
    screen.fill(STANDARD_COLOR)
    # Update player position
    player.update()
    # Update ghost position
    ghost.control()
    ghost.update()
    # Draw sprites
    sprite_list.draw(screen)
    # Draw the maze
    board.draw_maze(screen)
    # Update screen
    pygame.display.flip()
    # Treats player interaction
    for event in pygame.event.get():
        done = treats_event(event)