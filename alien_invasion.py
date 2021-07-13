import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Alien Invasion')

		self.settings = Settings()
	
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.ship = Ship(self)

		self.bullets = pygame.sprite.Group()
		

	def run_game(self):
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update()
			self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				else:
					if event.type == pygame.KEYDOWN:
						self._keydown_events(event)
					elif event.type == pygame.KEYUP:
						self._keyup_events(event)

	def _keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			self.fire_bullet()

	def _keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def fire_bullet(self):
		self.bullets.add(Bullet(self))

	def _update_screen(self):
			self.screen.fill(self.settings.bg_color)
			self.ship.draw_ship()
			for bullet in self.bullets:
				bullet.draw_bullet()
			pygame.display.flip()



if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()