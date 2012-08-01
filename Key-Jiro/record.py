import pygame, sys
from pygame.locals import *

pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.mixer.init()

scr = pygame.display.set_mode((300,300))
loop = 1
file = open(sys.argv[1],"w")
clk = pygame.time.Clock()
while loop:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				loop = 0
			if event.key == K_d:
				file.write("100000\n")
			if event.key == K_f:
				file.write("010000\n")
			if event.key == K_g:
				file.write("001000\n")
			if event.key == K_h:
				file.write("000100\n")
			if event.key == K_j:
				file.write("000010\n")
			if event.key == K_k:
				file.write("000001\n")
			if event.key == K_SPACE:
				file.write("000000\n")
