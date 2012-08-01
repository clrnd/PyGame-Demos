#!/usr/bin/env python
import pygame, random, time, psyco

w = 800
h = 600
psyco.full()
class Jorge:
	def __init__(self, scr):
		self.touch = []
		self.lices = 5
		self.level = 1
		self.lifes = 3
		self.vel_x = 0
		self.vel_y = 0
		self.x = 0
		self.y = 0
		self.img = pygame.image.load("boat.png")
		self.scr = scr
	def move(self, dir_x, dir_y):
		self.x += dir_x
		self.y += dir_y
		#self.draw()
	def jump(self):
		self.y += -20
		#self.draw()
	#def lvl(self):
	#	pygame.draw.rect(self.scr,(self.level*10,255/self.level,self.level+20),(0,h-100,w,h))
	def enemy(self):
		pygame.draw.polygon(self.scr,(150,0,200),((200,200),(250,250),(200,150))) # HACER ENEMYS
	def life(self):
		self.lifes -= 1
		self.x = 0
		self.y = 0
	def draw(self):
		self.scr.fill((0,0,0))
		#if self.scr.get_at((self.x+201,self.y+201)) == (100,100,50):
			#self.x -= 1
		if self.y+100 > h:
			self.life()
		if self.x > w:
			self.x =-50
			self.level += 1
			#self.lvl()
		self.y += 10
		#if self.scr.get_at((1,self.y+90)) != (0,0,0,255):
			#self.y -= 10
		if self.y < -50:
			self.y += 10
		if self.x < -50:
			self.x += 10
		self.enemy()
		self.touch = []
		for a in range(1,101,10):
			for b in range(1,101,10):
				try:
					self.touch.append(self.scr.get_at((self.x+a,self.y+b)))
				except:
					pass
		if (150,0,200,255) in self.touch:
			self.life()
		self.scr.blit(self.img,(self.x,self.y))
		#self.lvl()
		#pygame.draw.rect(self.scr,(100,100,50),(0,h-100,w,h))
		pygame.display.flip()

def main():
	x = 0
	y = 0
	scr=pygame.display.set_mode((w,h))
	pygame.mouse.set_visible(False)
	jorge = Jorge(scr)
	clk = pygame.time.Clock()
	while True:
		#pygame.time.delay(10)
		clk.tick(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				return
		key = pygame.key.get_pressed()
		#if key[pygame.K_DOWN]:
			#jorge.move(scr, 0, 5)
		if key[pygame.K_UP]:
			jorge.jump()
		if key[pygame.K_LEFT]:
			jorge.move(-10, 0)
		if key[pygame.K_RIGHT]:
			jorge.move(10, 0)
		jorge.draw()

if __name__ == '__main__':
	main()

