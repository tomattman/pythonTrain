import math

class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return math.hypot(self.x, self.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == oher.y

	def __repr__(self):
		return "Point({0.x!r}, {0.y!r})".format(self)

	def __str__(self):
		return "({0.x!r}, {0.y!r})".format(self)

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x = self.x + other.x
		self.y = self.y + other.y
		return self

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __isub__(self, other):
		self.x = self.x - other.x
		self.y = self.y - other.y
		return self

	def __mul__(self, other):
		return Point(self.x * other.x, self.y * other.y)

	def __imul__(self, other):
		self.x = self.x * other.x
		self.y = self.y * other.y
		return self

	def __truediv__(self, other):
		return Point(self.x / other.x, self.y / other.y)

	def __itruediv__(self, other):
		self.x = self.x / other.x
		self.y = self.y / other.y
		return self

	def __floordiv__(self, other):
		return Point(self.x // other.x, self.y // other.y)

	def __ifloordiv__(self, other):
		self.x = self.x // other.x
		self.y = self.y // other.y
		return self



class Circle(Point):
	def __init__(self, radius, x = 0, y = 0):
		super().__init__(x, y)
		self.radius = radius
	@property	
	def edge_distance_from_origin(self):
		return abs(self.distance_from_origin() - self.radius)

	@property	
	def area(self):
		return math.pi * (self.radius ** 2)

	def circumferense(self):
		return 2 * math.pi * self.radius

	def __eq__(self, other):
		return self.radius == other.radius and super().__eq__(other)

	def __repr__(self):
		return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)

	def __str__(self):
		return repr(self)

	@property
	def radius(self):
		"""Радиус окружности
		>>> circle = Circle(2)
		Traceback (most recent call last):
		...
		AssertionError: radius must be nonzero and nonnegative
		>>> circle = Circle(4)
		>>> circle.radius = 1
		Traceback (most recent call last):
		...
		AssertionError: radius must be nonzero and nonnegative
		>>> circle.radius = 6
		"""
		return self.__radius
	@radius.setter
	def radius(self, radius):
		assert radius > 0, "radius be nonzero and non-negative"
		self.__radius = radius
