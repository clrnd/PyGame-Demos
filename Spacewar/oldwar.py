import pygame
from pygame.locals import *
from random import randint
from math import *

scr = pygame.display.set_mode((800,600))
w,h = scr.get_size()
clk = pygame.time.Clock()
radian = pi/(360*0.5)

class Ship(pygame.sprite.Sprite):
	def __init__(self, pos, keys, angle, player):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("ship_"+player+".bmp")
		self.orig = self.image
		self.image.set_colorkey((0,0,0))

		self.rect = self.image.get_rect()
		self.rect.center = pos

		self.u, self.d, self.r, self.l = keys
		self.spd = 0
		self.angle = angle
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[self.u]:
			self.spd += 0.2 if self.spd < 5 else 0
		if keys[self.d]:
			self.spd -= 0.1 if self.spd > -2 else 0
		if keys[self.r]:
			tmp = self.rect.center
			self.angle = (self.angle+5)%360
			self.image = pygame.transform.rotozoom(self.orig,-self.angle-90,1)
			#self.image = pygame.transform.rotate(self.orig,-self.angle-90)
			self.image.set_colorkey((0,0,0))
			self.rect = self.image.get_rect()
			self.rect.center = tmp
		if keys[self.l]:
			tmp = self.rect.center
			self.angle = (self.angle-5)%360
			self.image = pygame.transform.rotozoom(self.orig,-self.angle-90,1)
			#self.image = pygame.transform.rotate(self.orig,-self.angle-90)
			self.image.set_colorkey((0,0,0))
			self.rect = self.image.get_rect()
			self.rect.center = tmp
		self.rect.centerx += cos(self.angle*radian)*self.spd
		self.rect.centery += sin(self.angle*radian)*self.spd

group = pygame.sprite.RenderUpdates()
group.add(Ship((50,50),(K_UP,K_DOWN,K_RIGHT,K_LEFT),-90,"1"))
loop = True
while loop:
	for e in pygame.event.get():
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					loop = False
	scr.fill((0,0,0))
	group.update()
	rects = group.draw(scr)
	pygame.display.update(rects)
	clk.tick(50)
