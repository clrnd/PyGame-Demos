import pygame
from pygame.locals import *
from random import randint, choice

pygame.font.init()
scr = pygame.display.set_mode((800,600))
w,h = scr.get_size()
font = pygame.font.Font(None,30)
SPEED = 3
INT = 10
ALIVE = True
BACK = [0,0,0,255]

class Chario(pygame.sprite.Sprite):
	def __init__(self, kontrols):
		pygame.sprite.Sprite.__init__(self)
		self.color = [200,200,0]
		self.image = pygame.surface.Surface((20,40))
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.centerx = w-10
		self.rect.centery = h/2
		self.falling = True
		self.yspd = 0
		self.xspd = 0
		self.u, self.l, self.r = kontrols
		self.points = 0
	def update(self):
		keys = pygame.key.get_pressed()
		# Horizontal
		if -10 < self.xspd < 10:
			if keys[self.r]: self.xspd += 2
			if keys[self.l]: self.xspd -= 2
		# Jump
		if keys[self.u] and not self.falling: self.yspd -= 20
		if self.falling and self.yspd < 30:
			self.yspd += 1
		self.xspd += 0.5 if self.xspd < 0 else -0.5
		# Correction
		if -1 < self.xspd < 1: self.xspd = 0
		# Actual movement
		self.rect.y += self.yspd
		if not self.falling: self.rect.x -= SPEED
		self.rect.x += self.xspd
		# Borders
		if self.rect.centerx < 0:
			self.rect.centerx = 1
		if self.rect.centerx > w:
			self.rect.centerx = w-1
		# Freefall
		try:
			#print scr.get_at((self.rect.centerx,self.rect.bottom)),self.rect.centerx,self.rect.bottom, BACK
			if list(scr.get_at((self.rect.centerx,self.rect.bottom))) != BACK:
				while list(scr.get_at((self.rect.centerx,self.rect.bottom+1))) != BACK:
					self.rect.centery -= 1
				self.falling = False
				self.yspd = 0
			if list(scr.get_at((self.rect.centerx,self.rect.bottom+2))) != BACK:
				self.falling = False
				self.yspd = 0
			else:
				self.falling = True
		except:
			self.falling = True
		# Psychedelic
		border = pygame.surface.Surface([x-2 for x in self.rect.size])
		self.image.fill([randint(0,255) for x in range(3)])
		for a in range(len(self.color)):
			rnd = choice((-1,1))
			if not 0 < self.color[a]+(rnd*INT) < 255: rnd *= -1
			self.color[a] += rnd*INT
		border.fill(self.color)
		self.image.blit(border,(1,1))
		# Falling
		if self.rect.top > h:
			self.points -= 1000
			self.rect.midtop = w/2,0
			self.yspd = 0
clk = pygame.time.Clock()

class Choflo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((100,20))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.left = w
		self.rect.y = randint(0,h)
		self.speed = randint(SPEED,SPEED+5)
		self.flag = False
	def update(self):
		if self.flag:
			self.image.fill((0,0,0))
			self.flag = False
		else:
			self.image.fill((255,255,255))
			self.flag = True
		self.rect.x -= self.speed
		self.rect.y += randint(-INT/2,INT/2)
		if self.rect.right < 0: self.kill()
		if self.rect.top > h: self.kill()

class Piso(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		size = randint(50,100),randint(50,100)
		self.image = pygame.surface.Surface(size)
		self.image.fill((255,255,255))
		border = pygame.surface.Surface([size[x]-2 for x in range(len(size))])
		border.fill([randint(0,255) for x in range(3)])
		self.image.blit(border,(1,1))
		self.rect = self.image.get_rect()
		self.rect.left = w
		self.rect.y = randint(h-200,h)
	def update(self):
		self.rect.x -= SPEED
		if self.rect.right < 0: self.kill


SEC = pygame.USEREVENT
pygame.time.set_timer(SEC,1000)
PISO = pygame.USEREVENT+1
pygame.time.set_timer(PISO,500)

chario = Chario((K_UP,K_LEFT,K_RIGHT))

choflos = pygame.sprite.RenderUpdates()
choflos.add(Choflo())

pisos = pygame.sprite.RenderUpdates()
pisos.add(Piso())

frames = 0
changed = False
loop = True
while loop:
	for e in pygame.event.get():
		if e.type == KEYDOWN and e.key == K_ESCAPE:
			loop = False
		if e.type == KEYDOWN and e.key == K_z:
			INT += 1
		if e.type == KEYDOWN and e.key == K_a:
			SPEED += 1
		if e.type == SEC:
			#print frames
			frames = 0
		if e.type == PISO:
			pisos.add(Piso())

	frames += 1
	#if randint(0,20) == 5: pisos.add(Piso())

	if randint(INT*5,100) == INT*5:
		choflos.add(Choflo())
		for a in range(len(BACK)-1):
			rnd = choice((-1,1))
			if not 0 < BACK[a]+(rnd*INT) < 255: rnd *= -1
			BACK[a] += rnd*INT
			scr.fill(BACK)
			changed = True

	chario.points += 0.1 * (INT+SPEED)

	#for obj in pisos:
		#if obj.rect.collidepoint(chario.rect.centerx,chario.rect.bottom-1):
			#chario.falling = False
			#chario.yspd = 0
			#while obj.rect.collidepoint(chario.rect.centerx,chario.rect.bottom):
				#chario.rect.y -= 1
			#break
		##if obj.rect.collidepoint(chario.rect.centerx,chario.rect.bottom+2):
			##chario.falling = False
			##chario.ypsd = 0
			##break
		#elif not obj.rect.collidepoint(chario.rect.centerx,chario.rect.bottom-2):
			#chario.falling = True
	#if chario.rect.collidelist([x.rect for x in pisos]) != -1:
		#chario.falling = False
		#chario.yspd = 0
	#else:
		#chario.falling= True
	#if pygame.sprite.spritecollideany(chario,pisos):
		#chario.falling = False
		#chario.yspd = 0
	#else:
		#chario.falling = True

	scr.fill(BACK)

	pisos.update()
	rects = pisos.draw(scr)

	txt = font.render("Score: "+str(int(chario.points)),1,(200,200,200),BACK)
	rects.append(scr.blit(txt,(0,0)))

	choflos.update()
	rects += choflos.draw(scr)

	rects.append(list(chario.rect))
	chario.update()
	rects.append(scr.blit(chario.image,chario.rect))

	if changed:
		pygame.display.update(rects)
		changed = False
	else:
		pygame.display.flip()
		changed = False
	clk.tick(50)
