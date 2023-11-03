import pygame
import time

pygame.init()


FPS = 60
ELLOW = 255,255,100
W = 1200
H = 800

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Test_Viki")
#pygame.display.set_icon(pygame.image.load('icon.bmp'))

sun_surf = pygame.image.load('1.png')
sun_rect = sun_surf.get_rect()
#geroi = pygame.image.load('верблюд_право.png')
#geroi_rect = sun_surf.get_rect()
#screen.blit(sun_surf, sun_rect)

x = 30
y = 610
speed = 5
jump = 20

clock = pygame.time.Clock()
Flag = True
flLeft = flRight = False


while Flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			Flag = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x -= speed
	elif keys[pygame.K_RIGHT]:
		x += speed


	screen.blit(sun_surf, sun_rect)
	pygame.draw.rect(screen, ELLOW, (x,y,50,100), 2)
	pygame.display.update()


	clock.tick(FPS)




