import pygame
from time import *
from pygame.locals import *

pygame.font.init()
w = 640
h = 480
scr = pygame.display.set_mode((w,h))
font = pygame.font.Font(None, 50)
scr.fill((30,30,30))
loop = 1
bounce = 0
x = 100
y = 100
dirx = 1
diry = 1
clk = pygame.time.Clock()

while loop:
	for e in pygame.event.get():
		if e.type == QUIT:
			loop = 0
		if e.type == KEYDOWN:
			if e.key == K_UP:
				if dirx < 1:
					dirx-=1
				else:
					dirx+=1
				if diry < 1:
					dirx-=1
				else:
					diry+=1
			elif e.key == K_DOWN:
				if dirx < 1:
					dirx+=1
				else:
					dirx-=1
				if diry < 1:
					diry+=1
				else:
					diry-=1
			else:
				loop = 0
	scr.fill((30,30,30))
	txt = font.render(str(localtime()[3])+":"+str(localtime()[4])+":"+str(localtime()[5]),1,(200,200,50))
	pygame.draw.rect(scr,(200,50,50),(w/2-25,h/2-25,50,50))
	if x+txt.get_width() > w-5:
		bounce=0
		dirx*=-1
	if x <= 5:
		bounce=0
		dirx*=-1
	if y+txt.get_height() > h-5:
		bounce=0
		diry*=-1
	if y <= 5:
		bounce=0
		diry*=-1
	try:
		if not bounce:
			for a in range(x,x+txt.get_width(),10):
				if scr.get_at((a,y)) != (30,30,30,255):
					diry*=-1
					bounce=1
				if scr.get_at((a,y+txt.get_height())) != (30,30,30,255):
					diry*=-1
					bounce=1
		if not bounce:
			for b in range(y,y+txt.get_height(),10):
				if scr.get_at((x,b)) != (30,30,30,255):
					dirx*=-1
					bounce=1
				if scr.get_at((x+txt.get_width(),b)) != (30,30,30,255):
					dirx*=-1
					bounce=1
	except:
		pass
	x+=dirx
	y+=diry
	scr.blit(txt,(x,y))
	pygame.display.flip()
	clk.tick(160)
