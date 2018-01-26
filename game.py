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
from enemy import Enemy
from vector import Vector
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
	end_coord = level.get_end_coord()

	player = Player(start)
	players = pygame.sprite.Group()
	players.add(player)

	enemy1 = Enemy((40,40))
	enemy2 = Enemy((140,340))
	enemies = pygame.sprite.Group()
	enemies.add(enemy1)
	enemies.add(enemy2)
	speed1 = 1
	speed2 = 1
	enemy1.patrol_setup( [(Vector(speed1,0), (40,40)),(Vector(0,speed1),(80,40)),
		(Vector(-speed1,0),(80,80)),(Vector(0,-speed1),(0,80)),(Vector(speed1,0),(0,0)),
		(Vector(0,speed1),(120,0)),(Vector(speed1,0),(120,100)),(Vector(-speed1,0),(200,100)),
		(Vector(0,-speed1),(120,100)),(Vector(-speed1,0),(120,0)),(Vector(0,speed1),(0,0)),
		(Vector(speed1,0),(0,80)),(Vector(0,-speed1),(80,80)),(Vector(-speed1,0),(80,40))
		])
	enemy2.patrol_setup([
		(Vector(speed2,0),(140,340)),(Vector(0,speed2),(260,340)),(Vector(speed2,0),(260,380)),
		(Vector(0,-speed2),(340,380)),(Vector(speed2,0),(340,280)),(Vector(0,-speed2),(360,280)),
		(Vector(-speed2,0),(360,240)),(Vector(0,-speed2),(340,240)),(Vector(0, speed2),(340,180)),
		(Vector(speed2,0),(340,240)),(Vector(0,speed2),(360,240)),(Vector(-speed2,0),(360,280)),
		(Vector(0,speed2),(340,280)),(Vector(-speed2,0),(340,380)),(Vector(0,-speed2),(260,380)),
		(Vector(-speed2,0),(260,340))
		])
	#GAME LOOP
	game_end = False
	win = False
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

		if player.coord() == end_coord and not win:
			level = Level(SCREEN_RESOLUTION, os.path.join("levels", "youwin"))
			win = True

		enemy1.patrol()
		enemy2.patrol()
		# DRAW
		canvas.fill(DARK_BLUE)
		level.walls.draw(canvas)
		level.floors.draw(canvas)
		level.ends.draw(canvas)
		players.draw(canvas)
		enemies.draw(canvas)

		clock.tick(60)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main("level1.lvl")

	