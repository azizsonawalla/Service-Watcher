class Host:

	def __init__(self, name):
		self.name = name
		self.last_status = False

	def get_name(self):
		return self.name

	def get_last_status(self):
		return self.last_status

	def set_name(self, name):
		self.name = name

	def set_last_status(self, status):
		self.last_status = status