import pygame
import os
from Board import Board
from Player import Player
from random import randint

class Goal(pygame.sprite.Sprite):
    def __init__(self, board: Board, player: Player):
        pygame.sprite.Sprite.__init__(self)
        self.board = board
        self.player = player
        self.catch = False
        img = pygame.image.load(os.path.join('images', 'redghost.png')).convert()
        self.image = pygame.transform.scale(img, (25, 25))
        self.rect = self.image.get_rect()

    def set_position(self) -> None:
        """ Define the spawn position based on the free spaces
                Parameters:
                        None
                Returns:
                        None
        """
        n = randint(0, len(self.board.free_spaces) - 1)
        self.rect = self.board.free_spaces[n]
        self.board.free_spaces.pop(n)

    def update(self) -> None:
        """Checks collision with the player
                Parameters:
                        None
                Returns:
                        None
        """
        if self.catch == False and pygame.Rect.colliderect(self.rect, self.player.rect):
            self.player.free()
