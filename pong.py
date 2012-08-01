#!/usr/bin/env python
import pygame
from pygame.locals import *
from random import randint,choice

scr = pygame.display.set_mode((800,600))
w,h = scr.get_size()

class Cholo:
	def __init__(self,kontrol,pos):
		self.img = pygame.Surface((10,100))
		self.img.fill((255,255,255))
		self.x,self.y = pos
		self.up,self.down = kontrol
	def update(self):
		keys = pygame.key.get_pressed()		#Handle keyboard and move "Pad"
		if keys[self.up]: self.y -= 9
		elif keys[self.down]: self.y += 9
		if self.y < 0: self.y = 0
		elif self.y+self.img.get_height() > h: self.y = h-self.img.get_height()
		scr.blit(self.img,(self.x,self.y))

class Ball:
	def __init__(self):
		self.radius = 10
		self.color = (randint(0,255),randint(0,255),randint(0,255))
		self.x = w/2
		self.y = h/2
		self.xdir = choice((-1,1))
		self.ydir = choice((-1,1))
		self.spd = 2
		self.bounce = 100
		self.bota = 0
	def draw(self):
		self.x += int(round(self.xdir*self.spd))
		self.y += int(round(self.ydir*self.spd))
		self.bounce += 1 if self.bounce < 101 else 0
		try:		#Bounce balls if they touch the "Pads" (color diferent from background)
			if (scr.get_at((self.x-self.radius,self.y+self.radius)) != (0,0,0,255) or scr.get_at((self.x+self.radius,self.y+self.radius)) != (0,0,0,255)) and self.bounce > 100:
				self.xdir *= -1
				self.bounce = 1
		except: pass		#Balls also bounce between them in a buggy/random way
		if self.y-self.radius < 0 or self.y+self.radius > h: self.ydir *= -1
		pygame.draw.circle(scr,self.color,(self.x,self.y),self.radius)
		if self.x < 0: return 2
		elif self.x > w: return 1
		else: return 0

p1 = Cholo((K_a,K_z),(10,h/2))
p2 = Cholo((K_UP,K_DOWN),(800-20,h/2))
bola = [Ball()]
loop = 0
while not loop:
	if 1 == randint(0,700): bola += [Ball()]
	scr.fill((0,0,0))
	p1.update()
	p2.update()
	for a in range(len(bola)):		#Update balls in the array
		loop = bola[a].draw()
		if loop: break
	pygame.display.flip()
	for e in pygame.event.get():
		if e.type == KEYDOWN and e.key == K_ESCAPE or e.type == QUIT:
			loop = 3
pygame.time.wait(500)
if loop != 3: print "Player %i Winns" % (loop)
