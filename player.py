#!/usr/bin/python3
# -*- coding: utf-8 -*-

### LABYRINT
### MODULE: PLAYER
### AUTHOR: Milan Welser
### EMAIL: welsemil@fel.cvut.cz

import pygame
from vector import Vector
import os

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('img','player.png'))
		self.r = 17
		#self.image.fill((120,120,0))
		self.rect = self.image.get_rect()
		self.rect.center = (pos[0] + 8.5, pos[1] + 8.5)
		self.rect.inflate_ip(-2,-2)
		self.vel = Vector(0,0)


	def update_vel(self, up=False, down=False, left=False, right=False):
		"""
		up, down, left, right: Boolean (true/false)
		"""
		if up:
			self.vel += Vector(0,-1)
		if down:
			self.vel += Vector(0,1)
		if left:
			self.vel += Vector(-1,0)
		if right:
			self.vel += Vector(1,0)
		self.vel.restrict(2) #velocity maximum
		#move forward and backward at the same time means dont move
		if not(up or down) or (up and down):
			self.vel.y = 0
		if not(left or right) or (left and right):
			self.vel.x = 0

	def stay_on_screen(self):
		"""
		Keeps player within the screen
		"""
		if (self.rect.x + self.r) > SCREEN_WIDTH:
			self.rect.x = SCREEN_WIDTH - self.r
		if (self.rect.x) < 0:
			self.rect.x = 0
		if (self.rect.y + self.r) > SCREEN_HEIGHT:
			self.rect.y = SCREEN_HEIGHT - self.r
		if (self.rect.y) < 0:
			self.rect.y = 0

	def move(self):
		self.rect.x += self.vel.x
		self.rect.y += self.vel.y

	def coord(self):
		return (self.rect.x // 20, self.rect.y // 20)