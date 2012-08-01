#! /usr/bin/env python

# Plot random pixels on the screen.

import pygame
import random

# Window dimensions
width = 640
height = 400
LEFT=1

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
flag=1
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			flag = False
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
			x,y=event.pos
			r=random.randint(0,255)
			g=random.randint(0,255)
			b=random.randint(0,255)
			screen.set_at((x,y),(r,g,b))
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
			screen.fill((0,0,0))
		pygame.display.flip()
