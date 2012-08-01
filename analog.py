import pygame, serial
from pygame.locals import*

scr = pygame.display.set_mode((1024,768),FULLSCREEN)
w,h = scr.get_size()
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.readline()
ser.readline()
ser.readline()

rect = pygame.surface.Surface((20,20))
rect.fill((200,200,0))
x = w/2
y = h/2
xmid = 510
ymid = 510

loop = True
while loop:
	for e in pygame.event.get():
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				loop = False
	num = ser.readline()
	if num[0] == "x":
		axis = 1
	if num[0] == 'y':
		axis = 0
	try:
		if axis:
			value = (xmid-int(num[1:]))/50
			if 0 < x+value < w:
				x += value
		else:
			value = (ymid-int(num[1:]))/50
			if 0 < y+value < h:
				y += value
	except:
		pass
	num = ser.readline()
	if num[0] == "x":
		axis = 1
	if num[0] == 'y':
		axis = 0
	try:
		if axis:
			value = (xmid-int(num[1:]))/50
			if 0 < x+value < w:
				x += value
		else:
			value = (ymid-int(num[1:]))/50
			if 0 < y+value < h:
				y += value
	except:
		pass
	scr.fill((0,0,0))
	scr.blit(rect,(x,y))
	pygame.display.flip()
pygame.quit()
ser.close()
