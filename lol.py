import pygame, math, random
from pygame.locals import *

scr = pygame.display.set_mode((1024,768), FULLSCREEN)
w,h = scr.get_size()
ang = 0
clk = pygame.time.Clock()
pygame.mouse.set_visible(False)
img = pygame.image.load("cat.bmp")
img.set_colorkey((255,0,0))
color = []
for a in range(90):
    color.append([int(random.randint(0,255)) for x in range(3)])
loop = True
while loop:
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                loop = False
    scr.fill((0,0,0))
    ang += 0.5
#    x2 = random.randint(0,w)
#    y2 = random.randint(0,h)
    rect = []
    for a in range(90):
        x = math.cos(math.radians(ang+a*2*2))*10000
        y = math.sin(math.radians(ang+a*2*2))*10000
        pygame.draw.line(scr, (255,255,255), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),(pygame.mouse.get_pos()[0]+x,pygame.mouse.get_pos()[1]+h/2+y),5)
#        pygame.draw.line(scr, color[a], (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),(pygame.mouse.get_pos()[0]+x,pygame.mouse.get_pos()[1]+h/2+y),5)
#        pygame.draw.line(scr, color[a], (x2,y2),(x2+x,y2+h/2+y),5)
    tmp = pygame.transform.rotozoom(img,ang*2*2,1)
#    tmp = pygame.transform.rotate(img,ang*2*2)
    scr.blit(tmp,(pygame.mouse.get_pos()[0]-tmp.get_width()/2,pygame.mouse.get_pos()[1]-tmp.get_height()/2))
#    scr.blit(tmp,(random.randint(0,w),random.randint(0,h)))
    clk.tick(60)
    pygame.display.flip()
