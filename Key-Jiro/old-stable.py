#!/usr/bin/env python
#A Guitar Hero attempt in Python (DIOS-CULEBRA)
import pygame

w = 640
h = 480
loop = 1
x = 52
y = -300
Y = 0
arry = []
tmp = 0
slot = 0
c = 0
#class Fichin:
#	def __init__(self,txt):
#		self.txt = txt
#	def draw(self):
#		for k in self.txt:
#			x += 76
#			if k = 1:
#				pygame.draw.circle(scr,(100,100,200),(x,y),30)
scr = pygame.display.set_mode((w,h))
a = open("cosa","r")
for k in a:
	for m in k:
		arry.append(m)
pygame.draw.rect(scr,(250,150,50),((90,0),(w-180,h)))
#print arry
clk = pygame.time.Clock()
stuff = []
while tmp < len(arry):
	if arry[tmp] == '\n':
		y += 62
		x = 52
		c = 0
	elif arry[tmp] == '0':
		x+= 76
		c += 1
	elif arry[tmp] == '1': 
		x += 76
		c += 1
		stuff.append((x,y,c))
	tmp += 1
while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			loop = 0
	scr.fill((0,0,0))
	pygame.draw.rect(scr,(250,150,50),((90,0),(w-180,h)))
	for p in stuff:
		color = {1:(255,0,0),2:(50,50,200),3:(50,200,200),4:(250,70,70),5:(200,50,200),6:(50,200,50)}
		pygame.draw.circle(scr,color[p[2]],(p[0],p[1]+Y),30)
	Y += 5
	clk.tick(30)
	pygame.display.flip()
