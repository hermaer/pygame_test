import pygame
from ball import Bullet
from params import W, H, RED, GREEN, BLUE, BLACK, WHITE, x_heroi, y_heroi, FPS, speed, x_bullet, speed_bullet, ground, jump_force, move  

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Viki_1.0.0")
pygame.time.set_timer(pygame.USEREVENT, 2000)
sun_surf = pygame.image.load('1.png').convert()
sun_rect = sun_surf.get_rect()


bullets = pygame.sprite.Group()
bullets.add(Bullet(x_bullet, y_heroi, "пуля.png", speed_bullet, x_heroi))


sun_surf = pygame.image.load('1.png').convert()
sun_rect = sun_surf.get_rect()


geroi_right = pygame.image.load('верблюд_право.png').convert_alpha()
geroi_left = pygame.transform.flip(geroi_right, 1, 0)
verb = geroi_right
geroi_rect = geroi_left.get_rect(center=(x_heroi, y_heroi))


Flag = True
while Flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			Flag = False

	bt = pygame.key.get_pressed()
	if bt[pygame.K_LEFT]:
		verb = geroi_left
		geroi_rect.x -= speed
		if geroi_rect.x < 0:
			geroi_rect.x = 0

	elif bt[pygame.K_RIGHT]:
		verb = geroi_right
		geroi_rect.x += speed
		if geroi_rect.x > W - geroi_rect.height:
			geroi_rect.x = W - geroi_rect.height

	elif bt[pygame.K_UP]:
		move = -jump_force

	elif move <= jump_force:
		if geroi_rect.bottom + move < ground:
			geroi_rect.bottom += move
			if move < jump_force:
				move += 1
		else:
			geroi_rect.bottom = ground
			move = jump_force + 1

	elif bt[pygame.K_SPACE]:
		x_bullet = x_heroi + speed
		bullets.draw(screen)
	
			


	bullets.update(W)
	screen.blit(sun_surf, sun_rect)
	screen.blit(verb, geroi_rect)
	pygame.display.update()
	clock.tick(FPS)



