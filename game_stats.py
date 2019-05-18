class GameStats(object):
	"""docstring for GameStats"""
	def __init__(self, ai_settings):
		super(GameStats, self).__init__()
		self.ai_settings = ai_settings
		self.reset_stats()

		#rang you xi yi kai shi chu yu fei huo dong zhuang tai 
		self.game_active = False
		self.high_score = 0

	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		self.game_active = True
		