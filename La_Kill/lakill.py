import pygame,random,time,sys
from pygame.locals import *

#Init
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
w = 1024
h = 768
scr = pygame.display.set_mode((w,h),(pygame.FULLSCREEN))
#scr = pygame.display.set_mode((w,h))
pygame.display.set_caption('Kill the Idiotas')
if len(sys.argv) < 2:
	pause = 1000
elif len(sys.argv) > 1:
	pause = sys.argv[1]

def Put(rnd,score):
	scr.fill((0,0,5))
	x,y = random.randint(0,w-200),random.randint(0,h-200)
	scr.blit(indx[rnd],(x,y))
	text = font.render(("Score: "+str(score)), 1, (200,200,100))
	scr.blit(text,(1,1))
	pygame.display.flip()

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
indx = [pygame.image.load("bush.png"),pygame.image.load("roger.png"),pygame.image.load("amd.jpg"),pygame.image.load("tux.png")]
for a in indx:
	a.convert_alpha()

scr.fill((50,50,50))
text = font.render("Alvare-ClrnD", 1, (50,50,250),(50,50,50))
text2 = font_big.render("Kill all the idiotas.", 1, (250,250,50),(50,50,50))
scr.blit(text2,(w/2-200,h/2-20))
scr.blit(text,(5,h-50))
pygame.display.flip()
loop=1
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
loop=1
score=0
scr.fill((0,0,5))
scr.blit(indx[1],(w/2-100,h/2-100))
pygame.display.flip()
rnd = 0
clk = pygame.time.get_ticks()
#pygame.mouse.set_visible(0)
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
pygame.mixer.music.play(-1)

while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
			loop = 0
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			mouse_x,mouse_y=event.pos
			r,g,b,a=scr.get_at((mouse_x,mouse_y))
			if (r,g,b) != (0,0,5):
				if rnd == 3:
					print "idiota"
					score -= 1
					idiot.play()
				else:
					print "yeah"
					score += 1
					yeah.play()
				rnd = random.randint(0,3)
				Put(rnd,score)
				clk = pygame.time.get_ticks()
			shot.play()
	if (pygame.time.get_ticks()-clk) > int(pause):
		if rnd != 3:
			score -= 1
			print "idiota"
		clk = pygame.time.get_ticks()
		rnd = random.randint(0,3)
		Put(rnd,score)
	if score > 20:
		scr.fill((0,0,0))
		pygame.display.flip()
		pygame.mixer.music.fadeout(2000)
		pygame.time.wait(2000)
		scr.fill((0,0,0))
		text = font.render("You Kinda Win Hijo Puta !!!", 1, (250,50,50),(0,0,0))
		scr.blit(text,(w/2-150,h/2-10))
		pygame.display.flip()
		win.play()
		win2.play()
		pygame.time.wait(3000)
		loop=0
	if score < 0:
		scr.fill((0,0,0))
		pygame.display.flip()
		pygame.mixer.music.fadeout(2000)
		pygame.time.wait(2000)
		scr.fill((0,0,0))
		text = font.render("You LOOSER !!!!!!!!", 1, (50,250,50),(0,0,0))
		scr.blit(text,(w/2-120,h/2-10))
		pygame.display.flip()
		looser.play()
		pygame.time.wait(3000)
		loop=0
print "Score = ",score
