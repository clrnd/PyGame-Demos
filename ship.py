import pygame, math
from pygame.locals import *

class Ship:
    def __init__(self):
        self.image=pygame.Surface((40, 40))
        self.rect=self.image.get_rect(center=(320,240))
        self.x=200
        self.y=150
        self.x_vel=0
        self.y_vel=0
        self.angle=0
        self.point_list = [(0, -20), (2.25, -20), (3.0, -6), (4.05, -20)]
    def update(self):
        self.rect.centerx=self.x
        self.rect.centery=self.y
        self.x+=self.x_vel
        self.y+=self.y_vel
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            self.angle -= 4
        if key[K_LEFT]:
            self.angle += 4
        if key[K_UP]:
            self.accel(0.1)
        if key[K_DOWN]:
            self.accel(-0.1)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image.fill((0, 0, 0))
	point_list = []
	self.angle2 = math.radians(self.angle)
	for p in self.point_list:
            radian, radius = p
            x = int(math.sin(radian+self.angle2)*radius)
            y = int(math.cos(radian+self.angle2)*radius)
	    point_list.append((x+self.image.get_width()/2,y+self.image.get_height()/2))
	pygame.draw.polygon(self.image, (255,255,255), point_list, 1)
    def accel(self, accel_speed):
        self.x_vel += math.sin(self.angle*2*math.pi/360)*-accel_speed
        self.y_vel += math.cos(self.angle*2*math.pi/360)*-accel_speed
    def wrap(self, surface):
        if self.x >= surface.get_width() + self.image.get_width()/2:
            self.x = -self.image.get_width()/2
        if self.x <= -self.image.get_width()/2 - 1:
            self.x = surface.get_width() + self.image.get_width()/2
        if self.y >= surface.get_height() + self.image.get_height()/2:
            self.y = -self.image.get_height()/2
        if self.y <= -self.image.get_height()/2 - 1:
            self.y = surface.get_height() + self.image.get_height()/2

def main():
    pygame.init()
    pygame.display.set_caption('trig demo.py')
    screen = pygame.display.set_mode((400, 300))
    ship = Ship()
    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)
        event = pygame.event.poll()
        if event.type == QUIT:
            return
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return

        screen.fill((0, 0, 0))
        ship.draw(screen)
        ship.update()
        ship.wrap(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
