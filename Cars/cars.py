import pygame
from math import *
from random import randint
from pygame.locals import *

radian = pi/(360*0.5)
scr = pygame.display.set_mode((640,480))
w,h = scr.get_size()
class Auto:
    def __init__(self,x,y,kontrol):
        self.x,self.y = (x,y)
        self.spd = 0
        self.angle = -90
        self.img = pygame.image.load('auto1.bmp').convert()
        self.img.set_colorkey((0,0,0))
        self.orig = self.img
        self.w,self.h = self.img.get_size()
        self.l,self.r,self.d,self.u = kontrol
        self.bounce = 0
    def update(self,area,vec):
        #INPUT
        keys = pygame.key.get_pressed()
        if keys[self.u]:
            self.spd += 0.1
        elif keys[self.d]:
            self.spd -= 0.1
        if keys[self.l]:
            self.angle = (self.angle-5)%360
            self.img = pygame.transform.rotozoom(self.orig,-self.angle-90,1)
            ##self.img = pygame.transform.rotate(self.orig,-self.angle-90)
            self.img.set_colorkey((0,0,0))
            self.w,self.h = self.img.get_size()
        elif keys[self.r]:
            self.angle = (self.angle+5)%360
            self.img = pygame.transform.rotozoom(self.orig,-self.angle-90,1)
            ##self.img = pygame.transform.rotate(self.orig,self.angle+90)
            self.img.set_colorkey((0,0,0))
            self.w,self.h = self.img.get_size()
    if keys[K_p]: #TODO TODO
        x1 = cos(self.angle*radian)*self.spd
        y1 = sin(self.angle*radian)*self.spd
        x2 = cos(vec[1]*radian)*vec[0]
        y2 = sin(vec[1]*radian)*vec[0]
        x3 = x1+x2
        y3 = y1+y2
        self.spd = abs(complex(x3,y3))
        self.angle = 270-atan(x1/x2)
        #Inertia 'n bla,bla
        if self.spd < -5 or self.spd > 5:
            self.spd -= 0.1*cmp(self.spd,0)
        if self.spd > 0:
            self.spd -= 0.05
        elif self.spd < 0:
            self.spd += 0.05
        if -0.05 < self.spd < 0.05:
            self.spd = 0
        #Collision !!
        self.bounce += 0 if self.bounce > 10 else 1
        if pygame.Rect(int(round(self.x-self.w/2)),int(round(self.y-self.h/2)),self.w,self.h).colliderect(area) and self.bounce > 10:
            if self.spd > 1 or self.spd < -1:
                self.spd *= -1
                self.bounce = 1
            else:
                self.spd = -0.5
        #Vect to Rect
        self.x += cos(self.angle*radian)*self.spd
        self.y += sin(self.angle*radian)*self.spd
        scr.blit(self.img,( int(round(self.x-self.w/2)) , int(round(self.y-self.h/2)) ))

car = Auto(200,100,(K_LEFT,K_RIGHT,K_DOWN,K_UP))
car2 = Auto(w-100,h-100,(K_a,K_d,K_s,K_w))
clk = pygame.time.Clock()
loop = True
while loop:
    scr.fill((50,50,50))
    obstacle = pygame.draw.rect(scr,(255,100,100),(w/2-25,h/2-25,50,50))
    car.update(obstacle,(car2.spd,car2.angle))
    car2.update(obstacle,(car.spd,car.angle))
    pygame.display.flip()
    clk.tick(50)
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            loop = False
        if e.type == KEYDOWN and e.key == K_c:
            scr.fill((50,50,50))
