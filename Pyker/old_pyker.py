#!/usr/bin/env python
#Alvare-ClrnD @ 3.52
#Yeah Yeah Python (DIOS CULEVRA)
import pygame
from pygame.locals import *
from random import randint,choice
from sys import argv

pygame.mixer.init(44100,-16,2,1024)
pygame.font.init()
font = pygame.font.Font(None,30)
Bfont = pygame.font.Font(None,80)
scr = pygame.display.set_mode((800,600))
w,h = scr.get_size()
music = True

class Bocha(pygame.sprite.Sprite):
	def __init__(self,maxs):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.surface.Surface((20,20))
		if randint(1,2) == 2:
			self.image.fill((30,30,200))
			self.good = False
		else:
			self.image.fill((30,200,30))
			self.good = True
		self.rect = self.image.get_rect()
		if randint(1,2) == 1:
			self.rect.centerx = randint(0,w)
			self.rect.y = choice((0-self.rect.h,h))
			self.xspd,self.yspd = 0,randint(2,maxs)
			if self.rect.y > 0:
				self.yspd *= -1
		else:
			self.rect.centery = randint(0,h)
			self.rect.x = choice((0-self.rect.w,w))
			self.xspd,self.yspd = randint(2,maxs),0
			if self.rect.x > 0:
				self.xspd *= -1
	def update(self):
		self.rect.y += self.yspd
		self.rect.x += self.xspd
		if self.rect.bottom < 0 or self.rect.top > h: self.kill()
		if self.rect.right+1 < 0 or self.rect.left > w: self.kill()

conter = 1
maxS = 3
score = 0
try:
	speed = int(argv[1])
except (ValueError,IndexError):
	speed = 60

bolas = pygame.sprite.RenderUpdates()
for a in range(2):
	bolas.add(Bocha(maxS))

player = pygame.sprite.Sprite()
player.image = pygame.surface.Surface((20,20))
player.image.fill((200,30,30))
player.rect = player.image.get_rect()
player.old = player.rect

try: #Intro
	txt = Bfont.render('Hiscore: '+file('hiscores','r').readline(),1,(200,200,200),(0,0,0))
except:
	txt = Bfont.render('Hiscore: 0',1,(200,200,200),(0,0,0))
scr.blit(txt,(w/2-txt.get_width()/2,h/2-txt.get_height()/2))
pygame.display.flip()
while pygame.event.poll().type not in [KEYDOWN,MOUSEBUTTONDOWN]: pass
scr.fill((0,0,0))
pygame.display.flip()
ticks = pygame.time.get_ticks()
clk = pygame.time.Clock()
pygame.mouse.set_visible(False)

if music: #Music
	pygame.mixer.music.load('aerodynamite.mp3')
	pygame.mixer.music.play()
	initiating = True
else: initiating = False

loop = True
while loop: ### MAIN LOOP ###
	for e in pygame.event.get():
		if e.type == KEYDOWN and e.key == K_ESCAPE:
			loop = False

	if randint(0,10) == 5: bolas.add(Bocha(maxS))

	if initiating: # Game speed change!
		if pygame.time.get_ticks() > 15000:
			speed = 50
		if pygame.time.get_ticks() > 19000:
			speed = 30
		if pygame.time.get_ticks() > 27000:
			speed = 10
		if pygame.time.get_ticks() > 33500:
			speed = 600
			initiating = False
			tocks = pygame.time.get_ticks() + 500
	if not initiating and music and pygame.time.get_ticks() - tocks > 500:
		if conter%2: speed = 30
		else: speed = 100
		conter += 1
		tocks = pygame.time.get_ticks() # end game speedchange.
	if pygame.time.get_ticks() - ticks > 20000:
		maxS += 1
		ticks = pygame.time.get_ticks()

	scr.fill((0,0,0))

	bolas.update()
	rects = bolas.draw(scr)

	txt = font.render("Score:"+str(score),1,(200,200,200),(0,0,0))
	scr.blit(txt,(0,0))
	rects.append((0,0,153,31))

	player.rect.center = pygame.mouse.get_pos()
	player.new = scr.blit(player.image,player.rect)
	rects.append(player.old)
	rects.append(player.new)
	player.old = player.new

	for a in pygame.sprite.spritecollide(player,bolas,True):
		if a.good:
			score += 1
		else:
			loop = False

	pygame.display.update(rects)
	clk.tick(speed)

srfc = pygame.Surface((w,h))
srfc.fill((0,0,0))
srfc.set_alpha(5)
if music:
	pygame.mixer.music.fadeout(1990)
for b in range(120):
	clk.tick(60)
	scr.blit(srfc,(0,0))
	pygame.display.flip()

try:
	fl = file("hiscores","rw")
	if score > int(fl.readline()):
		fl.write(str(score))
except:
	fl = file("hiscores","w")
	fl.write(str(score))

print "Score:",score,"\nTime:",pygame.time.get_ticks()/1000.0
