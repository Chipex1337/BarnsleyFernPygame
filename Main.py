import pygame
import random
import time

'''Please don't use this code to learn or anything, its garbage I suck at python, just needed to upload it for debugging'''

pygame.init()
pygame.display.set_caption("Fractal Fern Fun")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (58, 58, 58)

#Inits and colors finished

multiple = 32

SCREEN_WIDTH = 512*multiple
SCREEN_HEIGHT = 512*multiple
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)

offset = 103*multiple
x = 0
y = 0
n = 0

#Screen and variables created, change multiple to any number between 1 and 31 to change resolution
#fern placement changes accordingly

while n < 10000:
	pygame.draw.circle(screen, GREEN, (int(-46.25*multiple*x + SCREEN_WIDTH/2 - offset), int(-46.25*multiple*y + SCREEN_HEIGHT)), 0)
	pygame.draw.circle(screen, GREEN, (int(46.25*multiple*x + SCREEN_WIDTH/2 + offset), int(-46.25*multiple*y + SCREEN_HEIGHT)), 0)
	r = random.random()
	r = r * 100
	xn = x
	yn = y
	if r < 1:
		x = 0
		y = 0.16*yn
	elif r < 86:
		x = 0.85*xn+0.04*yn
		y = -0.04*xn+0.85*yn+1.6
	elif r < 93:
		x = 0.2*xn-0.26*yn
		y = 0.23*xn+0.22*yn+1.6
	else:
		x = -0.15*xn+0.28*yn
		y = 0.26*xn+0.24*yn+0.44
	#This if elif mess is from wikipedia https://en.wikipedia.org/wiki/Barnsley_fern
	#pygame.display.update()
	#pygame.display.flip()
	#Uncomment these if you want to see the plotting in real time (warning, slow!)
	n += 1
	if n%10000 == 0:
		print(n/10000)
		#This little thing gives you a rough idea of how much of the image is done
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

pygame.display.update()
pygame.display.flip()
pygame.image.save(screen, "FernIMG" + str(time.time()) + ".png")

#I use time.time() to differentiate between images