import pygame


class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, filename, speed, heroi_x):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect(center=(x, y))
		self.speed = speed
		self.heroi_x = heroi_x

	def update(self, *args):
		if self.rect.x < args[0] -20:
			self.rect.x += self.speed
		else:
			self.kill()
