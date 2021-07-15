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

		self.ship_x = float(self.rect.x)

	def draw_ship(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right:
			self.ship_x += self.settings.ship_speed
			self.rect.x = self.ship_x 
			if self.rect.right > self.screen_rect.right:
				self.rect.right = self.screen_rect.right
		elif self.moving_left:
			self.ship_x -= self.settings.ship_speed
			self.rect.x = self.ship_x 
			if self.rect.left < self.screen_rect.left:
				self.rect.left = self.screen_rect.left

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
