'''Solution to the 100 Doors Problem'''
from jinja2 import Environment, PackageLoader



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

	def toggle_door(self):
		self.is_open = not self.is_open
	
	def __repr__(self):
		return '%r' % self.is_open


def build_doors():	
	'''function to build the Doorsi, returns a list of doors'''
	#Create 100 closed doors
	n_doors = 100
	doors = []

	for door_id in range(n_doors):
		door = Door(door_id, False)
		doors.append(door)

	return doors

def pass_doors(doors, pass_number):
	'''walk past the doors and toggle every passs_number'th door'''
	for idx, door in enumerate(doors):
		if idx % pass_number == pass_number - 1:
			door.toggle_door()

	return doors







def do_doors():
	n_passes = 100
	doors = build_doors()
	pass_list = []
	pass_open_count = []

	pass_number = 0


	for pass_number in range(1,n_passes+1):
		doors = pass_doors(doors,pass_number)
		pass_list.append([door.is_open for door in doors])
		pass_open_count.append(sum([1 for door in doors if door.is_open==True]))
	




	print pass_list

	env = Environment(loader=PackageLoader('hundred_doors','templates'))

	template = env.get_template('door_template.html')

	html_string = template.render({'pass_list':pass_list, 'pass_open_count':pass_open_count,'enumerate':enumerate})

	
	with open('doors_solution.html','w') as html_file:
		html_file.write(html_string)






	
if __name__ == '__main__':

	do_doors()








