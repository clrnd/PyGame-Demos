#!/usr/bin/env python
import pygame,sys
from pygame.locals import *
from random import randint
from random import choice as unodestos
from time import time

size = (640,480)
bgcolor = (10,20,30)
try:
    dif = int(sys.argv[1])
except:
    dif = 50

#Clase
class Grn:
    def __init__(self,scren,spd,img):
        self.img = pygame.image.load(img)
        self.xy = [randint(0,size[0]-self.img.get_width()),randint(0,size[1]-self.img.get_height())]
        self.img.set_colorkey((255,255,255),RLEACCEL)
        self.vel = [randint(1,spd)*unodestos((-1,1)),randint(1,spd)*unodestos((-1,1))]
        self.scren = scren
        self.daing = 0
        self.dead = 0
        self.ttl = 0
    def update(self):
        if self.daing:
            self.ttl += 1
            self.img = pygame.transform.scale(self.img,(int(self.img.get_size()[0]/1.05),int(self.img.get_size()[1]/1.05,)))
        if self.ttl >= 50:
            self.img = pygame.Surface((1,1))
            print "dead"
            self.dead = 1
            self.daing = 0
            self.ttl = 0
        for a in [0,1]:
            if self.xy[a]+self.img.get_size()[a] > size[a] or self.xy[a] < 0:
                self.vel[a] *= -1
            self.xy[a] += self.vel[a]
        self.scren.blit(self.img,self.xy)
    def pos(self):
        return self.xy,self.img.get_size()

#Main
def main():
    scr = pygame.display.set_mode(size)

    #Sound
    pygame.mixer.init(44100,-16,2, 1024)
    shot = pygame.mixer.Sound('shot.ogg')
    bass = pygame.mixer.Sound('bass.ogg')
    hit = pygame.mixer.Sound('bass.ogg')

    #Fonts
    pygame.font.init()
    font = pygame.font.Font(None,60)

    #Selection
    txt = font.render('Choose level (1-9)',1,(200,200,100),(0,0,0))
    scr.blit(txt,(size[0]/2-txt.get_width()/2,size[1]/2-txt.get_height()/2))
    pygame.display.flip()
    loop = True
    while loop:
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if 49 <= e.key <= 57:
                    choice = e.key-48
                    loop = None
                elif e.key == K_ESCAPE:
                    return
            elif e.type == QUIT:
                return

    #Creation
    gay = [Grn(scr,choice,'green.bmp')]
    gey = Grn(scr,20,'red.bmp')
    gey.vel = [8*unodestos((-1,1)),8*unodestos((-1,1))]
##    base = []
##    for b in range(cant):
##        gay[b] = Grn(scr,choice,'green.bmp')
##        base += [1]

    #Main Loop
    clk = pygame.time.Clock()
    loop = True
    negro = True
    visible = None
    cant = 1
    calidad = time()
    while loop:
        scr.fill(bgcolor)
        for b in reversed(range(len(gay))):
            if gay[b].dead:
                del gay[b]
                cant -= 1
##                break
        if randint(1,dif) == randint(1,dif):
            gay += [Grn(scr,choice,'green.bmp')]
            cant += 1
        for b in range(len(gay)):
            gay[b].update()
        if negro:
            if randint(1,50) == randint(1,50):
                visible = False if visible else True
                gey.xy = [randint(0,size[0]-gey.img.get_width()),randint(0,size[1]-gey.img.get_height())]

##                if visible:
##                    visible = None
####                    del gey
##                else:
##                    visible = True
####                    gey = Grn(scr,10,'red.bmp')
        if visible:
            gey.update()
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    return
            elif e.type == MOUSEBUTTONDOWN:
                shot.play()
                touch = False
                for b in range(len(gay)):
                    p = gay[b].pos()
                    if p[0][0] <= pygame.mouse.get_pos()[0] <= p[0][0]+p[1][0] and p[0][1] <= pygame.mouse.get_pos()[1] <= p[0][1]+p[1][1]:
                        print 'hit'
                        gay[b].daing = 1
                        bass.play()
                        touch = True
                if visible and not touch:
                    p = gey.pos()
                    if p[0][0] <= pygame.mouse.get_pos()[0] <= p[0][0]+p[1][0] and p[0][1] <= pygame.mouse.get_pos()[1] <= p[0][1]+p[1][1]:
                        print 'king'
                        gey.daing = 1
                        hit.play()
                        negro = False
        if gey.dead:
            loop = False
            loose = False
        elif cant > 100:
            loop = False
            loose = True
        clk.tick(50)

    #Win
    if not loose:
        calidad = time() - calidad
        score = cant*choice - calidad
        txt = font.render('Score: '+str(score),1,(200,200,100),(100,40,120))
        scr.fill((100,40,120))
        scr.blit(txt,(size[0]/2-txt.get_width()/2,size[1]/2-txt.get_height()/2))
        pygame.display.flip()
    else:
        txt = font.render('Perdiste SORETE',1,(100,200,100),(200,40,20))
        scr.fill((200,40,20))
        scr.blit(txt,(size[0]/2-txt.get_width()/2,size[1]/2-txt.get_height()/2))
        pygame.display.flip()
        #TODO
    loop = True
    while loop:
        for e in pygame.event.get():
            if e.type in [KEYDOWN,QUIT,MOUSEBUTTONDOWN]:
                loop = False
if __name__ ==  '__main__':
    main()
import sys
sys.exit()
