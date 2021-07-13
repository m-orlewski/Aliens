import pygame

class Ship:
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('assets/ship.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

		self.settings = ai_game.settings

		self.moving_right = False
		self.moving_left = False

	def draw_ship(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right:
			self.rect.x += self.settings.ship_speed
		elif self.moving_left:
			self.rect.x -= self.settings.ship_speed
