#! /usr/bin/env python

# Move a worm across the screen. Beware of borders and self!

import pygame

class Worm:
	""" A worm. """

	def __init__(self, surface, x, y, length):
		self.surface = surface
		self.x = x
		self.y = y
		self.length = length
		self.dir_x = 0
		self.dir_y = -1
		self.body = []
		self.crashed = False

	def key_event(self, event):
		""" Handle key events that affect the worm. """
		if event.key == pygame.K_UP:
			self.dir_x = 0
			self.dir_y = -1
		elif event.key == pygame.K_DOWN:
			self.dir_x = 0
			self.dir_y = 1
		elif event.key == pygame.K_LEFT:
			self.dir_x = -1
			self.dir_y = 0
		elif event.key == pygame.K_RIGHT:
			self.dir_x = 1
			self.dir_y = 0

	def move(self):
		""" Move the worm. """
		self.x += self.dir_x
		self.y += self.dir_y
		
		r,g,b,a = self.surface.get_at((self.x,self.y))
		if (r,g,b) !=  (0,0,0):
			self.crashed = True

		self.body.insert(0, (self.x, self.y))

		if len(self.body) > self.length:
			self.body.pop()

	def draw(self):
		for x, y in self.body:
			#c = self.body.index((x,y))
			c=255
			self.surface.set_at((x, y), (c, c, c))

# Dimensions.
width = 640 
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# Our worm.
w = Worm(screen, width/2, height/2, 500)
#pygame.mixer.init()
#chomp = pygame.mixer.Sound("init.wav")
#chomp.play(20)
#color=[(range(1,201))]

while running:
	screen.fill((0, 0, 0))
	pygame.draw.line(screen,(200,20,20),(100,100),(100,200))
	w.move()
	w.draw()
	#if color <= 55:
	#	color = 255
	#color-=1

	if w.crashed or w.x <= 0 or w.x >= width-1 or w.y <= 0 or w.y >= height-1:
		print "Crash!"
		running = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			w.key_event(event)

	pygame.display.flip()
	clock.tick(140)
	#print w.body
