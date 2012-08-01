#! /usr/bin/env python
import pygame,sys
#import psyco
#psyco.full()

screen = pygame.display.set_mode((640,480))
event = pygame.event.poll()
r,g,b=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
print r,g,b
#for x,y in range(1,640),range(480,1,-1):
x=0
y=480
times=0
screen.fill((r,g,b))
while times<40:
	pygame.draw.line(screen,(0,40,255),(x,0),(0,y))
	x=x+16
	y=y-12
	times=times+1
	pygame.display.flip()
times=0
x=0
y=0
while times<40:
	pygame.draw.line(screen,(200,40,100),(0,y),(x,479))
	x=x+16
	y=y+12
	times=times+1
	pygame.display.flip()
times=0
x=0
y=479
while times<40:
	pygame.draw.line(screen,(50,200,100),(x,479),(639,y))
	x=x+16
	y=y-12
	times=times+1
	pygame.display.flip()
times=0
x=0
y=0
while times<40:
	pygame.draw.line(screen,(200,50,200),(x,0),(639,y))
	x=x+16
	y=y+12
	times=times+1
	pygame.display.flip()
while pygame.event.poll().type is not pygame.KEYDOWN: pass
