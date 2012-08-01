import pygame,random,sys
from pygame.locals import *

def main(speed=1):
	#Init
	pygame.mixer.pre_init(44100,-16,2, 1024)
	pygame.init()
	w = 800
	h = 600
	scr =  pygame.display.set_mode((w,h))
	pygame.display.set_caption("La Kill 2")
	pygame.mouse.set_cursor(*pygame.cursors.broken_x)
	#Movement Bounds
	x = w/2
	y = h/2
	dir_x = random.randint(-1,1)
	dir_y = random.randint(-1,1)
	leng = 0
	#Loading fonts
	font = pygame.font.Font(None, 36)
	font_big = pygame.font.Font(None, 66)
	#Loading sounds
	shot = pygame.mixer.Sound("shot.ogg")
	yeah = pygame.mixer.Sound("bass.ogg")
	idiot = pygame.mixer.Sound("idiot.ogg")
	win = pygame.mixer.Sound("win.ogg")
	win2 = pygame.mixer.Sound("win2.ogg")
	looser = pygame.mixer.Sound("looser.ogg")
	#Loading Images
	img = pygame.image.load("bush.png")
        img.convert_alpha()
	#Loading Clocks
	clk = pygame.time.Clock()

	scr.fill((50,50,50))
	text = font.render("Alvare-ClrnD", 1, (50,50,250),(50,50,50))
	text2 = font_big.render("La Kill 2", 1, (250,250,50),(50,50,50))
	scr.blit(text2,(w/2-100,h/2-20))
	scr.blit(text,(5,h-50))
	pygame.display.flip()
	loop=1	
	#pygame.time.delay(5000)
	while loop:
        	for event in pygame.event.get():
        	        if event.type == pygame.MOUSEBUTTONDOWN:
        	                if event.button == 1:
        	                        pygame.mixer.music.load("guitar.ogg")
        	                elif event.button == 3:
        	                        pygame.mixer.music.load("fondo.ogg")
        	                else:
        	                        try:
        	                                pygame.mixer.music.load("mexico.ogg")
        	                        except:
        	                                pygame.mixer.music.load("guitar.ogg")
        	                                pass
				loop = 0
			elif event.type == pygame.QUIT:
				loop = 0
	loop = 1
	scr.fill((50,50,50))
	score = 0
	bullets = 30
	pygame.mixer.music.play(-1)
	while loop and bullets:
		if leng > random.randint(10,300):
			dir_x = random.randint(-1,1)	
			dir_y = random.randint(-1,1)	
			while dir_x == 0 and dir_y == 0: 
				dir_x = random.randint(-1,1)	
				dir_y = random.randint(-1,1)	
			leng = 0
		if x < 10:
			dir_x = 1
		if y < 10:
			dir_y = 1
		if x > w-109:
			dir_x = -1
		if y > h-109:
			dir_y = -1
		x += dir_x*speed
		y += dir_y*speed
		#if x > w or y > h:
		#	loop = 0
		leng += 1
		scr.fill((50,50,50))
		scr.blit(img,(x,y))
		text = font.render(("Hits: "+str(score)), 0, (200,100,100))
		text2 = font.render(("Bullets: "+str(bullets)), 1, (100,100,200))
		scr.blit(text2,(1,1))
		scr.blit(text,(1,30))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
				loop = 0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				shot.play()
				bullets -= 1
				mouse_x,mouse_y=event.pos
				r,g,b,a=scr.get_at((mouse_x,mouse_y))
				if (r,g,b) != (50,50,50):
					score += 1
					yeah.play()
		#pygame.time.delay(500)
		clk.tick(100)
	print float(score)/pygame.time.get_ticks()*10000
	pygame.mixer.music.fadeout(2000)
	scr.fill((0,0,0))
	pygame.display.flip()
        text = font.render("Your Score is: "+str(float(score)/pygame.time.get_ticks()*10000), 1, (50,250,50),(0,0,0))
        scr.blit(text,(w/2-150,h/2-10))
	pygame.time.wait(3000)
        pygame.display.flip()
        looser.play()
        pygame.time.wait(3000)	
if __name__ == '__main__': 
	if len(sys.argv) > 1:
		main(int(sys.argv[1]))
	else:
		main()
