#!/usr/bin/python3
# -*- coding: utf-8 -*-

### LABYRINT
### MODULE: VECTOR 
### AUTHOR: Milan Welser
### EMAIL: welsemil@fel.cvut.cz

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		new = Vector(self.x + other.x, self.y + other.y)
		return new

	def __sub__(self, other):
		new = Vector(self.x - other.x, self.y - other.y)
		return new

	def mult(self,num):
		print("called on", self.x, self.y, "with num", num)
		x = num * self.x
		y = num * self.y
		print("ret",x,y)
		return Vector(x,y)

	def restrict(self, abs_value):
		"""
		Restricts the vector coordinates to stay within
		certain distance from 0
		"""
		if self.x < 0:
			self.x = -abs_value
		elif self.x > 0:
			self.x = abs_value
		if self.y < 0:
			self.y = -abs_value
		elif self.y > 0:
			self.y = abs_value