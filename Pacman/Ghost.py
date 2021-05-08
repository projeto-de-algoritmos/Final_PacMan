import pygame
import os
from Board import Board
from Player import Player

class Ghost(pygame.sprite.Sprite):
    def __init__(self, board: Board, player: Player):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 60
        self.board = board
        self.player = player
        img = pygame.image.load(os.path.join('images', 'redghost.png'))
        self.image = pygame.transform.scale(img.convert(), (8, 8))
        self.rect = self.image.get_rect()

    def control(self) -> None:
        """Updates the ghost current moving direction
                Parameters:
                        x (int): horizontal movement direction
                        y (int): vertical movement direction
                Returns:
                        None
        """
        x = self.rect.x
        y = self.rect.y
        temp_x = -1 if x > self.player.rect.x else 1
        temp_y = -1 if y > self.player.rect.y else 1

        if temp_x > 0 and not self.path_check(x + 1, y):
            self.movex = 1
        elif temp_x < 0 and not self.path_check(x - 1, y):
            self.movex = -1
        else:
            self.movex = 0

        if temp_y > 0 and not self.path_check(x, y + 1):
            self.movey = 1
        elif temp_y < 0 and not self.path_check(x, y - 1):
            self.movey = -1
        else:
            self.movey = 0

    def path_check(self, x:int, y:int) -> bool:
        """Check ghost colision with player
                Parameters:
                        x (int): ghost x position
                        y (int): ghost y position
                Returns:
                        None
        """
        collision_rect = pygame.Rect(x, y, 8, 8)
        for i in range(len(self.player.board.squares)):
            if pygame.Rect.colliderect(collision_rect, self.player.board.squares[i]):
                return True

        return False

    def update(self) -> None:
        """Update Ghost position if there is no collision
                Parameters:
                        None
                Returns:
                        None
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey