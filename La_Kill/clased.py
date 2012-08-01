import pygame,random,sys
from pygame.locals import *

#Clases
class Put():
	def Ins(self):
		scr.fill((0,0,5))
		self.rnd = random.randint(0,3)
		self.x = random.randint(0,h-200)
		self.y = random.randint(0,w-200)
		scr.blit(indx[self.rnd],(self.x,self.y))
		text = font.render(("Score: "+str(score)), 1, (200,200,100))
		scr.blit(text,(1,1))
		pygame.display.flip()
	def Event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
				return 0
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_x,mouse_y = event.pos
				r,g,b,a = scr.get_at((mouse_x,mouse_y))
				if (r,g,b) != (0,0,5):
					if self.rnd == 3:
						print "Idiota"
						s
