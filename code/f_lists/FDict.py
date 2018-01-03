out = "none"

class FDict(object):
	def __init__(self):
		self.__keys = []
		self.__get_val = lambda self, x: out


	def add(self, key, value):
		prev = self.__get_val
		self.__get_val = lambda self,x: ((x == key) and value) or prev(self,x)
		self.__keys.append(key)


	def at(self, key):
		return self.__get_val(self,key)


	def len(self):
		return len(self.__keys)


	def FPrint(self):
		print "|",
		for i in self.__keys:
			print i, ": ", self.__get_val(self,i), " | ",
		print


	def count(self, value):
		count = 0
		for i in self.__keys:
			if (value == self.__get_val(self, i)):
				count += 1
		return count


	def values(self):
		values = []
		for i in self.__keys:
			values.append(self.__get_val(self,i))
		return values

	def remove(self, value):
		key_t = False
		for i in self.__keys:
			if (value == self.__get_val(self,i)):
				key_t = i
				break
		if (key_t):
			self.add(key_t, out)
			self.__keys = filter(lambda a: a != key_t, self.__keys)
			self.remove(value)


	def extend(self, fdict):
		temp_fdict = FDict()
		for i in fdict.__keys:
			if (i not in self.__keys):
				self.add(i, fdict.__get_val(fdict, i))



