class Dog():
	"""Simple dog model"""
	def __init__(self, name, age):
		"""init dog with name and age"""
		self.name = name
		self.age = age

	def sit(self):
		"""Dog sit"""
		print(self.name.title() + " is now sitting")

	def roll_over(self):
		"""Dog is rolling"""
		print(self.name.title() + " rolled over!")

dog = Dog("Bobik", 1)
dog.sit()
dog.roll_over()		