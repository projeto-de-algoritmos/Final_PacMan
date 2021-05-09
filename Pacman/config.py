import pygame
from colors import BLACK, LIGHTBLUE, STANDARD_COLOR

# Classes
from Board import Board
from Player import Player
from Grape import Grape
from Goal import Goal

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

# Player sprite
player = Player(board)
player.rect.x = 25
player.rect.y = 25

# Sprite list
sprite_list = pygame.sprite.Group()

# Fruits sprite
fruit_list = []
for i in range(80):
    grape = Grape(board, player)
    fruit_list.append(grape)
    sprite_list.add(grape)

# Goal
for i in range(3):
    goal = Goal(board, player)
    fruit_list.append(goal)
    sprite_list.add(goal)
player_movement = 3

sprite_list.add(player)
