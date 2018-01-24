#!/usr/bin/python3
# -*- coding: utf-8 -*-

### LABYRINT LEVEL MAKER
### MODULE: LVLMAKER
### AUTHOR: Milan Welser
### EMAIL: welsemil@fel.cvut.cz
import pygame
from level import Grid


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED =   (255,0,0)
GREEN = (0,255,0)
BLUE =  (0,0,255)
DARK_BLUE = (10,10,60)

vstup = input("Do you wish to edit an existing lvl? (y/n)")
if vstup == 'y':
	edi = input("Enter filename: ")
	grid = Grid(400,400, fname="levels/"+edi)
else:
	grid = Grid(400,400)

pygame.init()
canvas = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption("LABYRINT")
clock = pygame.time.Clock()
start_exist = False
end_exist = False

game_end = False
while not game_end:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_end = True

	canvas.fill(BLACK)
	for cell in grid.get_cells():
		pos = [cell[0]*20, cell[1]*20]
		if grid.is_wall(cell):
			color = [255,0,0]
		elif grid.grid[cell[1]][cell[0]] == '2':
			color = [0,255,0]
		elif grid.grid[cell[1]][cell[0]] == '3':
			color = [0,0,255]
		else:
			color = WHITE
		pygame.draw.rect(canvas, color, (pos, (19,19)))

	mouse_pressed = pygame.mouse.get_pressed()
	if mouse_pressed[0]:
		mouse_pos = pygame.mouse.get_pos()
		idx = int(mouse_pos[0]) // 20
		idy = int(mouse_pos[1]) // 20
		if(grid.grid[idy][idx] == '0'):
			grid.grid[idy][idx] = '1'
	elif mouse_pressed[2]:
		mouse_pos = pygame.mouse.get_pos()
		idx = int(mouse_pos[0]) // 20
		idy = int(mouse_pos[1]) // 20
		if(grid.grid[idy][idx] == '1'):
			grid.grid[idy][idx] = '0'
		elif(grid.grid[idy][idx] == '2'):
			grid.grid[idy][idx] = '0'
			start_exist = False
		elif(grid.grid[idy][idx] == '3'):
			grid.grid[idy][idx] = '0'
			end_exist = False
	elif mouse_pressed[1]:
		mouse_pos = pygame.mouse.get_pos()
		idx = int(mouse_pos[0]) // 20
		idy = int(mouse_pos[1]) // 20
		if not start_exist and grid.grid[idy][idx] != '3':
			start_exist = True
			grid.grid[idy][idx] = '2'
		elif start_exist and not end_exist and grid.grid[idy][idx] != '2':
			end_exist = True
			grid.grid[idy][idx] = '3'
		


	clock.tick(30)
	pygame.display.update()

pygame.quit()

save = input("Do you want to save the lvl? (y/n)")
if save == 'y':
	filename = input("Enter filename: ")
	tbw = ""
	for i in range(20):
		for j in range(20):
			tbw+=grid.grid[i][j]
			if j != 19:
				tbw+=" "
		tbw+='\n'
	with open("levels/"+filename, 'w', encoding="utf-8") as f:
		f.write(tbw)
