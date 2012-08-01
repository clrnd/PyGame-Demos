# Alvare-ClrnD
# Spacewar implementation in Python@Pygame
import pygame, math
from pygame.locals import *
from random import randint

pygame.font.init()
scr = pygame.display.set_mode((800,600))
w,h = scr.get_size()
shots = pygame.sprite.RenderUpdates()
font = pygame.font.Font(None, 40)
DELAY = 5
COUNT = 5
SPEED = 0.2

class Shot(pygame.sprite.Sprite):
	def __init__(self, pos, angle, player):
		pygame.sprite.Sprite.__init__(self)
		self.player = player
		self.image = pygame.image.load("laser"+self.player+".bmp")
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
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.x_vel = 0
		self.y_vel = 0
		self.angle = 0
		self.u, self.d, self.r, self.l, self.s = keys
		self.delay = 0
		self.life = 10
		self.shots = []
	def update(self):
		self.rect.centerx += round(self.x_vel)
		self.rect.centery += round(self.y_vel)
		self.delay += 1 if self.delay < DELAY+1 else 0
		try:
			self.shots.remove(0)
		except: pass
		for a in range(len(self.shots)): self.shots[a] -= 1
		if self.life < 0: self.kill()
		#Keys
		key = pygame.key.get_pressed()
		if key[K_g] and self.player == "1":
			#angle = math.atan((self.rect.centerx-w/2.0)/(self.rect.centery-w/2.0))
			angle = math.atan2(self.rect.centery-h/2.0,self.rect.centerx-w/2.0)
			print math.degrees(angle)
			#print math.sin(angle)*-math.sqrt(self.rect.centerx**2+self.rect.centery**2)
			self.x_vel += math.sin(angle)*900/math.sqrt(self.rect.centerx**2+self.rect.centery**2)
			self.y_vel += math.cos(angle)*900/math.sqrt(self.rect.centerx**2+self.rect.centery**2)
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
			self.x_vel += math.sin(math.radians(self.angle))*-SPEED
			self.y_vel += math.cos(math.radians(self.angle))*-SPEED
		if key[self.d]:
			self.x_vel += math.sin(math.radians(self.angle))*+SPEED/2
			self.y_vel += math.cos(math.radians(self.angle))*+SPEED/2
		if key[self.s] and self.delay > DELAY and len(self.shots) < COUNT:
			shots.add(Shot(self.rect.center, self.angle, self.player))
			self.delay = 0
			self.shots += [200]
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
ships.add(Ship((20,h/2),"1",(K_w,K_s,K_d,K_a,K_LSHIFT)))
ships.add(Ship((1*w/2,h/2),"2",(K_UP,K_DOWN,K_RIGHT,K_LEFT,K_RCTRL)))
#ships.add(Ship((2*w/3,h/2),"3",(K_UP,K_DOWN,K_RIGHT,K_LEFT,K_RCTRL)))
#ships.add(Ship((502,h/2),"4",(K_UP,K_DOWN,K_RIGHT,K_LEFT,K_RCTRL)))
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

	for hits in pygame.sprite.groupcollide(shots, ships, False, False).items():
		if hits[0].player is not hits[1][0].player:
			hits[1][0].life -= 1
			hits[0].kill()

	scr.fill((0, 0, 0))
	rects = []

	#Ships
	ships.update()
	rects += ships.draw(scr)

	#Shots
	shots.update()
	rects += shots.draw(scr)

	#Ending
	if len(ships) < 2:
		try:
			print "The Winner is player "+ships.sprites()[0].player+" !!!"
		except IndexError:
			print "Fucking Draw !!!"
		break

	#Text
	for ship in ships.sprites():
		txt = font.render("Life "+ship.player+": "+str(ship.life), 1, [c+20*ship.life for c in range(3)])
		tmp = scr.blit(txt, ((int(ship.player)-1)*w/len(ships.sprites()),1))
		tmp[2] += 100
		rects += [tmp]

	pygame.display.update(rects)
