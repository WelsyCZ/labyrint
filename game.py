#!/usr/bin/python3
# -*- coding: utf-8 -*-

### LABYRINT
### MODULE: GAME
### AUTHOR: Milan Welser
### EMAIL: welsemil@fel.cvut.cz

#---------------------------------------------------------------
import pygame
import os
from level import Level
from sprite import Wall 
from player import Player
from copy import deepcopy
#---------------------------------------------------------------
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED =   (255,0,0)
GREEN = (0,255,0)
BLUE =  (0,0,255)
DARK_BLUE = (10,10,60)

#---------------------------------------------------------------
def main(jmeno_urovne):
	#INIT PYGAME
	pygame.init()
	canvas = pygame.display.set_mode(SCREEN_RESOLUTION)
	pygame.display.set_caption("LABYRINT")
	icon = pygame.image.load(os.path.join("img","icon.png"))
	pygame.display.set_icon(icon)
	clock = pygame.time.Clock()

	#INIT LEVEL AND PLAYER
	level = Level(SCREEN_RESOLUTION, os.path.join("levels", jmeno_urovne))
	start = level.get_start()

	player = Player(start)
	players = pygame.sprite.Group()
	players.add(player)

	#GAME LOOP
	game_end = False
	while not game_end:
		#EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_end = True
		#KEYS
		keys = pygame.key.get_pressed()
		up = keys[pygame.K_UP]
		down = keys[pygame.K_DOWN]
		left = keys[pygame.K_LEFT]
		right = keys[pygame.K_RIGHT]

		# MOVEMENT
		temp = deepcopy(player)
		temp.update_vel(up=up, down=False, left=False, right=False)
		temp.move()
		hit = pygame.sprite.spritecollide(temp, level.walls, False)
		if not hit:
			player.update_vel(up=up, down=False, left=False, right=False)
			player.move()
		player.stay_on_screen()
		del(temp)
		temp = deepcopy(player)
		temp.update_vel(up=False, down=down, left=False, right=False)
		temp.move()
		hit = pygame.sprite.spritecollide(temp, level.walls, False)
		if not hit:
			player.update_vel(up=False, down=down, left=False, right=False)
			player.move()
		player.stay_on_screen()
		del(temp)
		temp = deepcopy(player)
		temp.update_vel(up=False, down=False, left=left, right=False)
		temp.move()
		hit = pygame.sprite.spritecollide(temp, level.walls, False)
		if not hit:
			player.update_vel(up=False, down=False, left=left, right=False)
			player.move()
		player.stay_on_screen()
		del(temp)
		temp = deepcopy(player)
		temp.update_vel(up=False, down=False, left=False, right=right)
		temp.move()
		hit = pygame.sprite.spritecollide(temp, level.walls, False)
		if not hit:
			player.update_vel(up=False, down=False, left=False, right=right)
			player.move()
		player.stay_on_screen()
		del(temp)

		# DRAW
		canvas.fill(DARK_BLUE)
		level.walls.draw(canvas)
		level.floors.draw(canvas)
		players.draw(canvas)

		clock.tick(60)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main("level1.lvl")

	