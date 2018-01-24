#!/usr/bin/python3
# -*- coding: utf-8 -*-

### LABYRINT
### MODULE: LEVEL
### AUTHOR: Milan Welser
### EMAIL: welsemil@fel.cvut.cz
import sys
from sprite import Wall
from sprite import Floor
import pygame

class Level:
	
	def __init__(self, resolution, fname = None):
		self.width = resolution[0]
		self.height = resolution[1]
		self.resolution = resolution
		self.grid = Grid(self.width, self.height, fname = fname)
		#self.grid.grid[5][5] = True
		self.walls = self.get_walls()
		self.floors = self.get_floors()

	def get_walls(self):
		walls = pygame.sprite.Group()
		for cell in self.grid.get_cells():
			if self.grid.is_wall(cell):
				pos = [cell[0]*self.grid.cell_size, cell[1]*self.grid.cell_size]
				wall = Wall(pos)
				walls.add(wall)
		return walls

	def get_floors(self):
		floors = pygame.sprite.Group()
		for cell in self.grid.get_cells():
			if not self.grid.is_wall(cell):
				pos = [cell[0]*self.grid.cell_size, cell[1]*self.grid.cell_size]
				floor = Floor(pos)
				floors.add(floor)
		return floors

	def get_start(self):
		for r in range(self.grid.h_cells):
			for c in range(self.grid.w_cells):
				if self.grid.grid[r][c] == '2':
					return (c*self.grid.h_cells, r*self.grid.w_cells)

		return (360,140)

	def get_end_coord(self):
		for r in range(self.grid.h_cells):
			for c in range(self.grid.w_cells):
				if self.grid.grid[r][c] == '3':
					return (c,r)




class Grid:
	def __init__(self, w, h, cell_size = 20, fname = None):
		self.cell_size = cell_size
		w_cells = self.w_cells = w // cell_size
		h_cells = self.h_cells = h // cell_size
		if fname != None:
			self.grid = self.read_grid(fname)
		else:
			self.grid = [['0' for j in range(h_cells)] for i in range(w_cells)]

	def read_grid(self, fname):
		with open(fname, "r", encoding='utf-8') as f:
			lines = f.readlines()
			newlines = []
			for line in lines:
				newline = line.split()
				newlines.append(newline)
		return newlines

	def _print(self):
		for r in range(self.h_cells):
			for c in range(self.w_cells):
				sys.stdout.write("%c " % self.grid[r][c])
			sys.stdout.write("\n")

	def get_cells(self):
		for r in range(self.h_cells):
			for c in range(self.w_cells):
				yield (c, r)

	def is_wall(self, pos):
		return (self.grid[pos[1]][pos[0]] == '1')
