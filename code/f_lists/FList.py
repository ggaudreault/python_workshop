#out = None
out = "none"


#CODE
# FList is a "functional list", i.e. a list or array, but implemented using lambda abstractions
# The usual list methods are also implemented, e.g. len, pop, count, remove, insert, etc.

class FList(object):
	def __init__(self):
		# We don't really need this value, it could be generated from self.len() but
		# it'll be more useful to have it for dictionnaries later and i'm hungry
		self.__length = 0
		self.__get_val = lambda self, x: out


	def add_next(self, value):
		prev = self.__get_val
		len_now = self.__length
		self.__get_val = lambda self,x: ((x == len_now) and value) or prev(self,x)
		self.__length += 1


	def at_index(self, index):
		return self.__get_val(self,index)


	def len(self):
		return self.__length


	def real_len(self):
		max = 0
		while (self.__get_val(self,max) != out):
			print max
			print self.__get_val(self, max)
			max += 1
		return max


	def pop(self):
		prev = self.__get_val
		self.__length -= 1
		len_prev = self.__length

		value = self.__get_val(self, len_prev)
		#print "l: ", len_prev
		self.__get_val  = lambda self, x: ((x == len_prev) and out) or prev(self,x)
		return value


	def move(self, limit, index, direction):
		if (direction *index) > (direction*limit):
			#print "in"
			prev = self.__get_val
			next_value = self.__get_val(self, index - direction)
			self.__get_val = lambda self, x: ((x == index) and next_value) or prev(self,x)
			self.move(limit, index - direction, direction)
		else:
			prev = self.__get_val
			self.__get_val = lambda self, x: ((x == index) and out) or prev(self,x)
			old_length = self.__length
			self.__length = old_length + direction


	def count(self, value):
		count = 0
		for i in range(self.__length):
			if (value == self.__get_val(self, i)):
				count += 1
		return count


	def remove(self, value):
		index = -1
		for i in range(self.__length):
			if (value == self.__get_val(self,i)):
				index = i
				break
		if (index >= 0):
			self.move(self.__length - 1, index, -1)
			self.remove(value)


	def insert(self, index, value):
		self.move(index, self.__length, 1)
		prev = self.__get_val
		self.__get_val = lambda self, x: ((x == index) and value) or prev(self,x)


	def first(self):
		return self.__get_val(self, 0)


	def get_first(self): # like pop() but start from beginning of flist
		prev = self.__get_val
		#self.__length -= 1

		value = self.__get_val(self, 0)
		#print "l: ", self.__length
		self.__get_val  = lambda self, x: ((x == 0) and out) or prev(self,x)
		self.move(self.__length - 1, 0, -1)
		return value


	def extend(self, flist):
		temp_flist = FList()
		total_length = self.len() + flist.len()
		temp_flist.__get_val = flist.__get_val
		while flist.len() != 0:
			value_to_add = flist.get_first()
			self.add_next(value_to_add)
		flist.__length = total_length
		flist.__get_val = temp_flist.__get_val


	def reverse(self):
		#print self.__length
		old_length = self.__length
		new_flist = FList()
		while self.len() != 0:
			value_to_add = self.pop()
			#print "v :", value_to_add
			new_flist.add_next(value_to_add)
		self.__get_val = new_flist.__get_val
		self.__length = old_length
		#print self.__length
		self.Fprint()


	def find_min(self):
		index = 0
		mini = self.__get_val(self,index)
		index += 1
		candidate = self.__get_val(self, index)
		while (candidate != out):
			if (mini > candidate):
				mini = candidate
			index += 1
			candidate = self.__get_val(self, index)
		return mini



	def sort(self):
		self.Fprint()
		new_flist = FList()
		temp_l = self.len()
		while self.len() != 0:
			print "len: ", self.len()
			mini = self.find_min()
			self.remove(mini)
			new_flist.add_next(mini)
		self.__length = temp_l
		self.__get_val = new_flist.__get_val


	def Fprint(self):
		#print dogg.len()
		print dogg.len()
		print "[",
		for i in range(self.__length - 1):
			print str(self.__get_val(self,i)) + ",",
		print self.__get_val(self,self.__length - 1),
		print "]"













#print dogg.get_val
#print dogg.length
"""dogg.add_next("catt")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "le: ", dogg.len()
dogg.remove("a")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "le: ", dogg.len()
dogg.insert(1, "boat")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "le: ", dogg.len()"""

"""
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
dog_pop = dogg.pop()
print "pop: ", dog_pop
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
dogg.add_next("bello")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
dogg.add_next("end")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "start rem: "
dogg.remove("a")
#dogg.remove1("a")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "done rem "
dogg.remove("a")
#dogg.remove1("a")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
dog_pop = dogg.pop()
print "pop: ", dog_pop
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "len: ", dogg.len()
dogg.add_next("bello")
#print dogg.count("bello")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "len: ", dogg.len()
dogg.remove("bello")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
#print dogg.count("bello")
print "len: ", dogg.len()
dogg.add_next("achi")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "len: ", dogg.len()
dogg.add_next("boat")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
dogg.insert(1, "catt")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
dogg.pop()
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
dogg.insert(1, "ok")
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]
print "len: ", dogg.len()
print dogg.first()
dogg.get_first()
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3)]

kitty = FList()
kitty.add_next("cat_1")
kitty.add_next("cat_2")
kitty.add_next("cat_3")
print [kitty.at_index(0), kitty.at_index(1), kitty.at_index(2)]
dogg.extend(kitty)
print "len: ", dogg.len()
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3), dogg.at_index(4), dogg.at_index(5), dogg.at_index(6)]

print [kitty.at_index(0), kitty.at_index(1), kitty.at_index(2)]
kitty.add_next("cat_1")
kitty.add_next("cat_2")
kitty.add_next("cat_3")
print [kitty.at_index(0), kitty.at_index(1), kitty.at_index(2)]
kitty.reverse()
print [kitty.at_index(0), kitty.at_index(1), kitty.at_index(2)]
print kitty.real_len()
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3), dogg.at_index(4), dogg.at_index(5), dogg.at_index(6)]
dogg.sort()
print [dogg.at_index(0), dogg.at_index(1), dogg.at_index(2), dogg.at_index(3), dogg.at_index(4), dogg.at_index(5), dogg.at_index(6)]
dogg.Fprint()

"""



