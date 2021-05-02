import pygame
from colors import BLACK, LIGHTBLUE, STANDARD_COLOR

# Classes
from Board import Board
from Player import Player

pygame.init()

screen_size = (1600,800)
screen = pygame.display.set_mode(screen_size)
screen.fill(BLACK) # Set background color

# Screen title
pygame.display.set_caption("PacMan")

# Create an object to help track time
clock = pygame.time.Clock()

# Objects
board = Board(25, 25, 32, 64, 0, STANDARD_COLOR)

# Sprite list
sprite_list = pygame.sprite.Group()
# Player sprite
player = Player(board)
player.rect.x = 13
player.rect.y = 13
sprite_list.add(player)
movement = 1