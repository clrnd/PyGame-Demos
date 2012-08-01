import pygame, serial
from pygame.locals import *

scr = pygame.display.set_mode((200,200))
w, h = scr.get_size()
srl = serial.Serial("/dev/ttyUSB0",9600)
clk = pygame.time.Clock()

loop = True
while loop:
	for e in pygame.event.get():
		if e.type == KEYDOWN and e.key == K_ESCAPE: loop = False
	keys = pygame.key.get_pressed()
	if keys[K_z]: srl.write('c')
	if keys[K_x]: srl.write('d')
	if keys[K_c]: srl.write('e')
	if keys[K_v]: srl.write('f')
	if keys[K_b]: srl.write('g')
	if keys[K_n]: srl.write('a')
	if keys[K_m]: srl.write('b')
	clk.tick(2000)
