import pygame
from pygame.locals import *
from random import randint,choice
from os import system

scr = pygame.display.set_mode((800,600))
pygame.display.set_caption("PyNvaders - Beta 2")
w,h = scr.get_size()
pygame.font.init()
font = pygame.font.Font(None,30)

class Alien(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((32,32))
		self.G = 200
		self.image.fill((100,self.G,140))
		self.rect = self.image.get_rect()
		if choice((True,False)):
			self.spd = 8
		else:
			self.spd = -8
			self.rect.right = w
		self.won = False
	def update(self):
		self.rect.x += self.spd
		if self.rect.right > w or self.rect.left < 0:
			self.spd *= -1
			self.rect.y += randint(self.rect.height,self.rect.height*3)
		if self.rect.bottom > h:
			self.won = True

class SAlien(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((32,32))
		self.image.fill((200,0,0))
		self.rect = self.image.get_rect()
		if choice((True,False)):
			self.spd = 10
		else:
			self.spd = -10
			self.rect.right = w
		self.won = False
		self.min = randint(0,w/3)
		self.max = randint(w/3*2,w)
	def update(self):
		self.rect.x += self.spd
		if (self.spd > 0 and self.rect.right > self.max) or (self.spd < 0 and self.rect.left < self.min):
			self.spd *= -1
			self.rect.y += randint(self.rect.height,self.rect.height*2)
		if self.rect.bottom > h:
			self.won = True

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((32,32))
		self.image.fill((200,200,200))
		self.rect = self.image.get_rect()
		self.rect.centerx = w/2
		self.rect.y = h-self.rect.height*2
	def update(self):
		oldrect = pygame.rect.Rect(self.rect)
		key = pygame.key.get_pressed()
		if key[K_RIGHT]:
			self.rect.x += 5 if self.rect.right < w else 0
		if key[K_LEFT]:
			self.rect.x -= 5 if self.rect.left > 0 else 0
		scr.blit(self.image,(self.rect.x,self.rect.y))
		return [oldrect,self.rect]

class Shot(pygame.sprite.Sprite):
	def __init__(self,xpos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((5,20))
		self.image.fill((200,40,40))
		self.rect = self.image.get_rect()
		self.rect.centerx = xpos
		self.rect.bottom = h-self.rect.height*2
	def update(self):
		self.rect.y -= 5
		if self.rect.top < 0:
			self.kill()

class Laser(pygame.sprite.Sprite):
	def __init__(self,xpos):
		pygame.sprite.Sprite.__init__(self)
		self.imag = [pygame.image.load("laser"+str(x)+".bmp") for x in range(1,9)]
#		self.image = self.imag[7]
#        	self.image.set_colorkey((255,255,255))
		self.rect = self.imag[0].get_rect()
		self.rect.centerx = xpos
		self.pic = 7
#		self.white = pygame.image.load("white.bmp")
	def update(self):
                if self.pic > 1:
                        self.pic -= 1
                        self.image = self.imag[self.pic]
                        self.image.set_colorkey((255,255,255))
                self.rect.centerx += randint(0,10) - 5
#                        self.image.set_colorkey((255,255,255))
		return [scr.blit(self.image,(self.rect))]

class AShot(pygame.sprite.Sprite):
	def __init__(self,alien):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((5,20))
		self.image.fill((0,200,200))
		self.rect = self.image.get_rect()
		self.rect.centerx = randint(alien.rect.centerx-20,alien.rect.centerx+20)
		self.rect.centery = alien.rect.centery
	def update(self):
		self.rect.y += 5
		if self.rect.bottom > h:
			self.kill()

txt = font.render("A: shoot - S: laser - ARROWS: move",1,(200,200,200))
scr.fill((0,0,0))
scr.blit(txt, (w/2-txt.get_rect().centerx,h/2-txt.get_rect().centery))
pygame.display.flip()
#while pygame.event.poll().type not in [KEYDOWN,MOUSEBUTTONDOWN]: pass

aliens = pygame.sprite.RenderUpdates()
aliens.add(Alien())
ship = Ship()
shots = pygame.sprite.RenderUpdates()
AShots = pygame.sprite.RenderUpdates()

loop = True
laser = False
shooting = False
reloadtime1 = 200
reloadtime2 = 10000
last1 = 0
last2 = pygame.time.get_ticks()
timeout = 0
lasering = False
score = 0
tempo = 60
clk = pygame.time.Clock()

while loop:
	for e in pygame.event.get():
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				loop = False
			elif e.key == K_a:
				shooting = True
			elif e.key == K_s and pygame.time.get_ticks() - last2 > reloadtime2 and not lasering:
				laser = Laser(ship.rect.centerx)
                                for p in range(0,w):
                                        scr.set_at((randint(0,w),randint(0,h)),(255,255,255))
                                        pygame.display.flip()
                                timeout = pygame.time.get_ticks()
                                lasering = True
                                tempo = 10
		elif e.type == KEYUP:
			if e.key == K_a:
				shooting = False

	if shooting and (pygame.time.get_ticks() - last1) > reloadtime1:
			last1 = pygame.time.get_ticks()
			shots.add(Shot(ship.rect.centerx))

	if randint(0,10) == 5:
		aliens.add(Alien())
	if randint(0,150) == 5:
		aliens.add(SAlien())
##	try:
##		if randint( 0,500/len( aliens.sprites() ) ) == 1:
##			AShots.add(AShot(aliens.sprites()[randint(0,len(aliens)-1)], ship))
##	except: pass

	for ET in aliens:
		if ET.won: loop = False
		if ET.rect.centerx - 5 < ship.rect.centerx < ET.rect.centerx + 5: AShots.add(AShot(ET))

	scr.fill((0,0,0))

	txt = font.render("Score: "+str(score)+"    ",1,(100,100,200))
	rects = [scr.blit(txt,(1,1))]
	
        if pygame.time.get_ticks() - last2 > reloadtime2:
                rects += [pygame.draw.circle(scr,(255,0,0),(w-25,h-25),7)]

	shots.update()
	rects += shots.draw(scr)
	AShots.update()
	rects += AShots.draw(scr)
	if laser:
                tempo += 1.5
		rects += laser.update()
		if pygame.sprite.spritecollide(laser,aliens,True):
			score += 1
		if pygame.time.get_ticks() - timeout > 2000:
                        scr.fill((0,0,0))
			pygame.display.update(rects)
			rects += rects
			laser = False
			lasering = False
                        last2 = pygame.time.get_ticks()
                        tempo = 60

	rects += ship.update()

	aliens.update()
	rects += aliens.draw(scr)

        #if pygame.sprite.groupcollide(shots,AShots,True,True): pass
	if laser and pygame.sprite.spritecollide(laser,AShots,True): pass
	if pygame.sprite.groupcollide(shots,aliens,True,True): score += 1
	if pygame.sprite.spritecollide(ship,AShots,True):
		loop = False
	pygame.display.update(rects)
	clk.tick(tempo)
tmp = pygame.Surface((w,h))
tmp.fill((0,0,0))
tmp.set_alpha(20)
for b in range(60):
    clk.tick(60)
    scr.blit(tmp,(0,0))
    pygame.display.flip()
txt = font.render("Score: "+str(score)+"    ",1,(200,200,200))
scr.fill((0,0,0))
scr.blit(txt, (w/2-txt.get_rect().centerx,h/2-txt.get_rect().centery))
pygame.display.flip()
while pygame.event.poll().type not in [KEYDOWN,MOUSEBUTTONDOWN]: pass
pygame.quit()
print "Score:",score
#system("pause")
