import string
import random

robots = []
def generate_name():
	return ''.join(random.choices(string.ascii_uppercase, k = 2))+str(''.join(random.choices(string.digits, k = 3)))

class Robot:
	def __init__(self):
		self.name = generate_name()
		while self.name in robots:
			self.name = generate_name()
		robots.append(self.name)
	
	def name(self):
		return self.name
	
	def reset(self):
		self.name = generate_name()
		while self.name in robots:
			self.name = generate_name()
		robots.append(self.name)