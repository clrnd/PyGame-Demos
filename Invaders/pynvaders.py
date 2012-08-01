import pygame
from pygame.locals import *
from random import randint as rnd

scr = pygame.display.set_mode((800,600))
w,h = scr.get_size()
X = [x for x in range(0,w,w/12)]
Y = [Y for Y in range(0,h/2,h/10)]
Mov = 1

class Alien(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((40,40))
		self.image.fill((100,100,0))
		self.rect = self.image.get_rect()
		self.col,self.row = x,y
		self.rect.topleft = (X[self.col],Y[self.row])
	def update(self):
		global Mov
		X[self.col] += Mov
		if not (0 < X[self.col] and X[self.col]+self.image.get_width() < w):
			Mov *= -1
			for c in range(len(Y)): Y[c] += 10
		self.rect.topleft = (X[self.col],Y[self.row])

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((32,32))
		self.image.fill((200,200,200))
		self.oldrect = self.rect = self.image.get_rect()
		self.rect.centerx = w/2
		self.rect.centery = h-self.rect.height*2
	def update(self):
		self.oldrect = pygame.rect.Rect(self.rect)
		key = pygame.key.get_pressed()
		if key[K_RIGHT]:
			self.rect.x += 5 if self.rect.right < w else 0
		if key[K_LEFT]:
			self.rect.x -= 5 if self.rect.left > 0 else 0
	def draw(self,_scr):
		_scr.blit(self.image,(self.rect.x,self.rect.y))
		return [self.oldrect,self.rect]

aliens = pygame.sprite.RenderUpdates()
for a in range(5):
	for b in range(10):
		aliens.add(Alien(b,a))
ship = Ship()

clk = pygame.time.Clock()

loop = True
while loop:
	for e in pygame.event.get():
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				loop = False
	scr.fill((0,0,0))

	aliens.update()
	ship.update()
	rects = aliens.draw(scr)
	rects += ship.draw(scr)
	pygame.display.update(rects)
	clk.tick(60)
