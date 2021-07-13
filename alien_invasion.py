import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Alien Invasion')

		self.settings = Settings()
	
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.ship = Ship(self)

		self.bullets = pygame.sprite.Group()

		self.aliens = pygame.sprite.Group()
		
		self._create_fleet()

	def run_game(self):
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
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
			self._fire_bullet()

	def _keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_limit:
			self.bullets.add(Bullet(self))

	def _update_bullets(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)

	def _update_screen(self):
			self.screen.fill(self.settings.bg_color)
			self.ship.draw_ship()
			for bullet in self.bullets:
				bullet.draw_bullet()

			self.aliens.draw(self.screen)

			pygame.display.flip()

	def _create_fleet(self):
		ship_height = self.ship.rect.height
		alien = Alien(self)

		alien_width = alien.rect.width
		alien_height = alien.rect.height

		available_space_x = self.settings.screen_width - (2 * alien_width)
		available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height

		aliens_x = available_space_x // (2 * alien_width)
		aliens_y = available_space_y // (2 * alien_height)

		for i in range(aliens_x):
			for j in range(aliens_y):
				self._add_alien(i, j)

	def _add_alien(self, i, j):
		alien = Alien(self)
		alien.x = (2 * i + 1) * alien.rect.width
		alien.y = (2 * j + 1) * alien.rect.height
		alien.rect.x = alien.x
		alien.rect.y = alien.y
		self.aliens.add(alien)

	def update(self):
		self.x += self.settings.alien_speed
		self.rect.x = self.x

	def _update_aliens(self):
		self.aliens.update()



if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()