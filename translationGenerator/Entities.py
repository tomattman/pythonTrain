
class Translation:
	def __init__(self, key, message, name=None):
		self.key = key
		self.message = message
		if name:
			self.name = name
		else:
			self.name = key

	@property
	def key(self):
		return self.__key

	@key.setter
	def key(self, key):
		self.__key = key

	@property
	def message(self):
		return self.__message

	@message.setter
	def message(self, message):
		self.__message = message

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	def __str__(self):
		return "translation(key - {0.key}, message - {0.message}, name - {0.name}".format(self)


class TranslationList:
	def __init__(self, folder = ""):
		self.folder = folder
		self.__translations = set()

	def add_item(self, translation):
		self.__translations.add(translation)

	@property
	def folder(self):
		return self.__folder
	@folder.setter
	def folder(self, folder):
		if folder[:1] == "\\":
			self.__folder = folder
		else:
			self.__folder = "\\" + folder
		

	@property
	def translations(self):
		return self.__translations

	def print_(self):
		print("Folder name: {0}".format(self.__folder))
		for tr in self.translations:
			print(tr)
