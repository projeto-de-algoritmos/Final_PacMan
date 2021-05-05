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
        self.images = []
        self.board = board
        self.player = player

        img = pygame.image.load(os.path.join('images', 'redghost.png')).convert()
        img = pygame.transform.scale(img, (8, 8))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self) -> None:
        """Updates the ghost current moving direction
                Parameters:
                        x (int): horizontal movement direction
                        y (int): vertical movement direction
                Returns:
                        None
        """
        if self.rect.x > self.player.rect.x:
            temp_x = -1
        else :
            temp_x = 1
        if self.rect.y > self.player.rect.y:
            temp_y = -1
        else :
            temp_y = 1

        x = self.rect.x
        y = self.rect.y
        if temp_x > 0 and self.path_check(x + 1, y) == False:
            self.movex = 1
        elif temp_x < 0 and self.path_check(x - 1, y) == False:
            self.movex = -1
        else :
            self.movex = 0

        if temp_y > 0 and self.path_check(x, y + 1) == False:
            self.movey = 1
        elif temp_y < 0 and self.path_check(x, y - 1) == False:
            self.movey = -1
        else :
            self.movey = 0

    def path_check(self, x:int, y:int) -> bool:

        collision_rect = pygame.Rect(x, y, 8, 8)

        for i in range(len(self.player.board.squares)):
            if pygame.Rect.colliderect(collision_rect, self.player.board.squares[i]):
                return True

        return False

    def update(self) -> None:
        """Update the  Player sprite(image) position if there is no collision
                Parameters:
                        None
                Returns:
                        None
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey