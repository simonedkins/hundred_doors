'''Solution to the 100 Doors Problem'''

class Door():
	'''Door Object'''
	door_id = None
	is_open = None

	def __init__(self,door_id=0, is_open=False):
		self.door_id = door_id
		self.is_open = is_open

	def open_door(self):
		'''Function to open the door'''
		self.is_open = True

	def close_door(self):
		'''Function to close the door'''
		self.is_open = False

	def change_door(self):
		self.is_open = not self.is_open













