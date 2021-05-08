import pygame
from colors import BLACK, LIGHTBLUE, STANDARD_COLOR

# Classes
from Board import Board
from Player import Player
from Ghost import Ghost
from Grape import Grape

pygame.init()

screen_size = (1600,800)
screen = pygame.display.set_mode(screen_size)
screen.fill(BLACK) # Set background color

# Screen title
pygame.display.set_caption("PacMan")

# Create an object to help track time
clock = pygame.time.Clock()

# Objects
board = Board(50, 50, 16, 32, 0, STANDARD_COLOR)
# Sprite list
sprite_list = pygame.sprite.Group()
# Player sprite
player = Player(board)
player.rect.x = 25
player.rect.y = 25
sprite_list.add(player)
player_movement = 3
# Ghost sprite
for i in range(5):
    ghost = Ghost(board, player)
    ghost.rect.x = 26
    ghost.rect.y = 26
    sprite_list.add(ghost)
# Fruits sprite
fruit_list = []
for i in range(5):
    grape = Grape(board, player)
    fruit_list.append(grape)
    sprite_list.add(grape)