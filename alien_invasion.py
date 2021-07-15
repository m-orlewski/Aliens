import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Alien Invasion')

		self.settings = Settings()
	
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.stats = GameStats(self)

		self.ship = Ship(self)

		self.bullets = pygame.sprite.Group()

		self.aliens = pygame.sprite.Group()
		
		self._create_fleet()

		self.play_button = Button(self, "Play")
		self.sb = Scoreboard(self)

	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()

			if self.stats.game_active:
				self.ship.update()
				self._update_aliens()
				self._update_bullets()

	def _check_events(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					self._check_play_button(mouse_pos)
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

		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()
			self.sb.check_high_score() 

		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

			self.stats.level += 1
			self.sb.prep_level()

	def _update_screen(self):
			self.screen.fill(self.settings.bg_color)
			self.ship.draw_ship()
			for bullet in self.bullets:
				bullet.draw_bullet()

			self.aliens.draw(self.screen)

			self.sb.show_score()

			if not self.stats.game_active:
				self.play_button.draw_button()

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
		self._check_fleet_edges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _ship_hit(self):
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			self.sb.prep_ships()

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
			
		if button_clicked and not self.stats.game_active:
			pygame.mouse.set_visible(False)

			self.settings.initialize_dynamic_settings()

			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()
			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()