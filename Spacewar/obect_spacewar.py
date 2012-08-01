import pygame, math
from pygame.locals import *
from random import randint

scr = pygame.display.set_mode((800,600))
w,h = scr.get_size()
shots = pygame.sprite.RenderUpdates()

class Shot(pygame.sprite.Sprite):
	def __init__(self,pos, angle, player):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("laser"+player+".bmp")
		self.image = pygame.transform.rotozoom(self.image,angle,1)
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.x_vel = math.sin(angle*2*math.pi/360)*-5
		self.y_vel = math.cos(angle*2*math.pi/360)*-5
		self.time = 200
	def update(self):
		self.rect.centerx += self.x_vel
		self.rect.centery += self.y_vel
		self.time -= 1
		if self.time < 0: self.kill()
		#Wrapping
		if self.rect.centerx >= w + self.image.get_width()/2:
			self.rect.centerx = -self.image.get_width()/2
		if self.rect.centerx <= -self.image.get_width()/2 - 1:
			self.rect.centerx = w + self.image.get_width()/2
		if self.rect.centery >= h + self.image.get_height()/2:
			self.rect.centery = -self.image.get_height()/2
		if self.rect.centery <= -self.image.get_height()/2 - 1:
			self.rect.centery = h + self.image.get_height()/2

class Ship(pygame.sprite.Sprite):
	def __init__(self,pos,player,keys):
		pygame.sprite.Sprite.__init__(self)
		self.player = player
		self.image = pygame.image.load("ship_"+self.player+".bmp")
		self.image.set_colorkey((0,0,0))
		self.orig = self.image
		self.x,self.y = pos
		self.rect = self.image.get_rect()
		self.rect.center = self.x,self.y
		self.x_vel = 0
		self.y_vel = 0
		self.angle = 0
		self.u, self.d, self.r, self.l, self.s = keys
		self.delay = 0
		self.life = 10
	def update(self):
		self.rect.centerx += self.x_vel
		self.rect.centery += self.y_vel
		self.delay += 1
		#Keys
		key = pygame.key.get_pressed()
		if key[self.r]:
			tmp = self.rect.center
			self.angle = (self.angle-5)%360
			self.image = pygame.transform.rotozoom(self.orig,self.angle,1)
			self.image.set_colorkey((0,0,0))
			self.rect = self.image.get_rect()
			self.rect.center = tmp
		if key[self.l]:
			tmp = self.rect.center
			self.angle = (self.angle+5)%360
			self.image = pygame.transform.rotozoom(self.orig,self.angle,1)
			self.image.set_colorkey((0,0,0))
			self.rect = self.image.get_rect()
			self.rect.center = tmp
		if key[self.u]:
			self.x_vel += math.sin(self.angle*2*math.pi/360)*-0.2
			self.y_vel += math.cos(self.angle*2*math.pi/360)*-0.2
		if key[self.d]:
			self.x_vel += math.sin(self.angle*2*math.pi/360)*+0.1
			self.y_vel += math.cos(self.angle*2*math.pi/360)*+0.1
		if key[self.s] and self.delay > 20:
			shots.add(Shot(self.rect.center, self.angle, self.player))
			self.delay = 0
		#Wrapping
		if self.rect.centerx >= w + self.image.get_width()/2:
			self.rect.centerx = -self.image.get_width()/2
		if self.rect.centerx <= -self.image.get_width()/2 - 1:
			self.rect.centerx = w + self.image.get_width()/2
		if self.rect.centery >= h + self.image.get_height()/2:
			self.rect.centery = -self.image.get_height()/2
		if self.rect.centery <= -self.image.get_height()/2 - 1:
			self.rect.centery = h + self.image.get_height()/2

pygame.display.set_caption('PySpacewar')

ships = pygame.sprite.RenderUpdates()
ships.add(Ship((500,500),"1",(K_UP,K_DOWN,K_RIGHT,K_LEFT,K_RCTRL)))
ships.add(Ship((100,100),"2",(K_w,K_s,K_d,K_a,K_LSHIFT)))
clk = pygame.time.Clock()
loop = True

while loop:
	clk.tick(60)
	event = pygame.event.poll()
	if event.type == QUIT:
		loop = False
	if event.type == KEYDOWN:
		if event.key == K_ESCAPE:
			loop = False

	#TODO
	#for hit in pygame.sprite.groupcollide(shots, ships, False, False):
		#print hit

	scr.fill((0, 0, 0))

	ships.update()
	rects = ships.draw(scr)

	shots.update()
	rects += shots.draw(scr)

	pygame.display.update(rects)
