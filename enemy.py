#!/usr/bin/python3
# -*- coding: utf-8 -*-

### LABYRINT
### MODULE: ENEMY
### AUTHOR: Milan Welser
### EMAIL: welsemil@fel.cvut.cz
import pygame
import os
from random import choice
from vector import Vector
import time
class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		name = choice(('green_enemy_16x17.png','pink_enemy_16x17.png'))
		self.image = pygame.image.load(os.path.join('img', name))
		self.rect = self.image.get_rect()
		self.rect.center = (pos[0] + 8, pos[1] + 8.5)
		self.vel = Vector(0,0)

	def move(self):
		self.rect.x += self.vel.x
		self.rect.y += self.vel.y

	def patrol_setup(self,path): # path: [(vel, coord), (vel,coord), ...]
		self.patrol_points = len(path)
		self.path = path
		self.current = 0
		self.backwards = False

		
	def patrol(self):
		my_pos = (self.rect.x, self.rect.y)
		if(my_pos == self.path[self.current][1]):
			self.vel = self.path[self.current][0]
			self.current += 1
			self.current = self.current % self.patrol_points


				
		self.move()