#!/usr/bin/python3
# -*- coding: utf-8 -*-

### LABYRINT
### MODULE: SPRITE
### AUTHOR: Milan Welser
### EMAIL: welsemil@fel.cvut.cz

import pygame
import os

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([20, 20])
        self.image = pygame.image.load(os.path.join('img','wall2.png'))
        #self.image.fill((100, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([20, 20])
        self.image = pygame.image.load(os.path.join('img','floor.png'))
        #self.image.fill((100, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos