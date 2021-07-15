class Settings:
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		self.ship_limit = 3

		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)

		self.bullets_limit = 5

		self.fleet_drop_speed = 10

		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.aliens_speed = 1.0

		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.aliens_speed *= self.speedup_scale

