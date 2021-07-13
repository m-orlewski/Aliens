class Settings:
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		self.ship_speed = 1

		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)

		self.bullets_limit = 5

		self.aliens_speed = 0.5
		self.fleet_drop_speed = 10
		self.fleet_direction = 1