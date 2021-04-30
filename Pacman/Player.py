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
        img = pygame.transform.scale(img, (10, 10))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        collide = False
        
        for i in range(len(self.board.squares)):
            if pygame.Rect.colliderect(self.rect, self.board.squares[i]):
                collide = True
        if collide == False:
            self.movex += x
            self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey