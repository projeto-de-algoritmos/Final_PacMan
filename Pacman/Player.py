import pygame
import os
from Board import Board

class Player(pygame.sprite.Sprite):
    def __init__(self, board: Board):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 60
        self.images = []
        self.board = board

        img = pygame.image.load(os.path.join('images', 'pacman.png')).convert()
        img = pygame.transform.scale(img, (16, 16))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x: int, y: int) -> None:
        """Updates the player current moving direction
                Parameters:
                        x (int): horizontal movement direction
                        y (int): vertical movement direction
                Returns:
                        None
        """
        self.movex += x
        self.movey += y

    def update(self) -> None:
        """Update the  Player sprite(image) position if there is no collision
                Parameters:
                        None
                Returns:
                        None
        """
        collision_rect = pygame.Rect(0, 0, 16, 16)
        # X collision check
        collide = False
        collision_rect.x = self.rect.x + self.movex
        collision_rect.y = self.rect.y
        
        for i in range(len(self.board.squares)):
            if pygame.Rect.colliderect(collision_rect, self.board.squares[i]):
                collide = True
        if collide == False:
            self.rect.x = self.rect.x + self.movex

        # Y collision check
        collide = False
        collision_rect.x = self.rect.x
        collision_rect.y = self.rect.y + self.movey
        
        for i in range(len(self.board.squares)):
            if pygame.Rect.colliderect(collision_rect, self.board.squares[i]):
                collide = True
        if collide == False:
            self.rect.y = self.rect.y + self.movey