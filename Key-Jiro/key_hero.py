#!/usr/bin/env python
#A Guitar Hero attempt in Python (DIOS-CULEBRA)
import pygame, sys
from pygame.locals import *

w = 640
h = 480
loop = 1
x = 52
cosa = sys.argv[1]
a = open(cosa,"r")
a = a.readlines()
y = -len(a)*69
Y = 0
arry = []
tmp = 0
slot = 0
c = 0
score = 0
alive = 0

pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.init()
fail = pygame.mixer.Sound("fail.ogg")
font = pygame.font.Font(None, 36)
scr = pygame.display.set_mode((w,h))
pygame.mixer.music.load("tema2.ogg")
a = open(cosa,"r")
for k in a:
	for m in k:
		arry.append(m)
clk = pygame.time.Clock()
stuff = []
while tmp < len(arry):
	if arry[tmp] == '\n':
		y += 69
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
color = {1:(255,0,0),2:(50,50,200),3:(50,200,200),4:(250,70,70),5:(200,50,200),6:(50,200,50)}
pygame.mixer.music.play()
flag = [0,0,0,0,0,0]
touch = [0,0,0,0,0,0]
caca = [1,1,1,1,1,1]
xpos = [x for x in range(128,509,76)]
while loop:
	scr.fill((0,0,0))
	pygame.draw.rect(scr,(250,150,50),((90,0),(w-180,h)))
	pygame.draw.line(scr,(200,50,201),(0,450),(639,450))
	for p in stuff:
		pygame.draw.circle(scr,color[p[2]],(p[0],p[1]+Y),30)
	current = []
	for f in xpos:
		current.append(scr.get_at((f,450)))
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			loop = 0
		if event.type == pygame.KEYDOWN:
			if event.key == K_d and not flag[0]:
				if (255,0,0,255) == current[0]:
					score += 1
					flag[0] = 1
					touch[0] = 0
					pygame.mixer.music.set_volume(1.0)
				else:
					score -= 2
					pygame.mixer.music.set_volume(0.3)
					#fail.play()
			elif event.key == K_f and not flag[1]:
				if (50,50,200,255) == current[1]:
					score += 1
					flag[1] = 1
					touch[1] = 0
					pygame.mixer.music.set_volume(1.0)
				else:
					score -= 2
					pygame.mixer.music.set_volume(0.3)
			elif event.key == K_g and not flag[2]:
				if (50,200,200,255) == current[2]:
					score += 1
					flag[2] = 1
					touch[2] = 0
					pygame.mixer.music.set_volume(1.0)
				else:
					score -= 2
					pygame.mixer.music.set_volume(0.3)
			elif event.key == K_h and not flag[3]:
				if (250,70,70,255) == current[3]:
					score += 1
					flag[3] = 1
					touch[3] = 0
					pygame.mixer.music.set_volume(1.0)
				else:
					score -= 2
					pygame.mixer.music.set_volume(0.3)
			elif event.key == K_j and not flag[4]:
				if (200,50,200,255) == current[4]:
					score += 1
					flag[4] = 1
					touch[4] = 0
					pygame.mixer.music.set_volume(1.0)
				else:
					score -= 2
					pygame.mixer.music.set_volume(0.3)
			elif event.key == K_k and not flag[5]:
				if (50,200,50,255) == current[5]:
					score += 1
					flag[5] = 1
					touch[5] = 0
					pygame.mixer.music.set_volume(1.0)
				else:
					score -= 2
					pygame.mixer.music.set_volume(0.3)
			#elif event.key == K_d or event.key == K_f or event.key == K_g or event.key == K_h or event.key == K_j or event.key == K_k and flag
	if current[0] != (255,0,0,255):
		flag[0] = 0
		caca[0] = 1
		if touch[0]:
			score -= 2
			pygame.mixer.music.set_volume(0.3)
			touch[0] = 0
	elif caca[0]:
		touch[0] = 1
		caca[0] = 0
	if current[1] != (50,50,200,255):
		flag[1] = 0
		caca[1] = 1
		if touch[1]:
			score -= 2
			pygame.mixer.music.set_volume(0.3)
			touch[1] = 0
	elif caca[1]:
		touch[1] = 1
		caca[1] = 0
	if current[2] != (50,200,200,255):
		flag[2] = 0
		caca[2] = 1
		if touch[2]:
			score -= 2
			pygame.mixer.music.set_volume(0.3)
			touch[2] = 0
	elif caca[2]:
		touch[2] = 1
		caca[2] = 0
	if current[3] != (250,70,70,255):
		flag[3] = 0
		caca[3] = 1
		if touch[3]:
			score -= 2
			pygame.mixer.music.set_volume(0.3)
			touch[3] = 0
	elif caca[3]:
		touch[3] = 1
		caca[3] = 0
	if current[4] != (200,50,200,255):
		flag[4] = 0
		caca[4] = 1
		if touch[4]:
			score -= 2
			pygame.mixer.music.set_volume(0.3)
			touch[4] = 0
	elif caca[4]:
		touch[4] = 1
		caca[4] = 0
	if current[5] != (50,200,50,255):
		flag[5] = 0
		caca[5] = 1
		if touch[5]:
			score -= 2
			pygame.mixer.music.set_volume(0.3)
			touch[5] = 0
	elif caca[5]:
		touch[5] = 1
		caca[5] = 0
#		if event.type == pygame.KEYUP:
#			if event.key == K_d and (scr.get_at((128,450)) != (255,0,0,255)):
#				flag[0] = 0
#			if event.key == K_f and (scr.get_at((128+76,450)) != (50,50,200,255)):
#				flag[1] = 0
	#hit = []
	#m = 128
	#for a in range(0,6):
	#	hit.append(scr.get_at((m,450)))
	#	m += 76
	#key = pygame.key.get_pressed()
	#if key[K_d]:
	#	if (255,0,0,255) == scr.get_at((128,450)): score += 1
	#	else: score -= 1
	#if key[K_f]:
	#	if (50,50,200,255) == scr.get_at((128+76,450)): score += 1
	#	else: score -= 1
	#if key[K_g]:
	#	if (50,200,200,255) == scr.get_at((128+76*2,450)): score += 1
	#	else: score -= 1
	txt = font.render("Score: "+str(score),1,(200,200,200))
	scr.blit(txt,(1,1))
	Y += 5
	clk.tick(58)
	pygame.display.flip()
print score
