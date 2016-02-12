####################  1-gram picking #####################


def get_count(texts):
	dic = {}
	for word in texts:
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
	#print dic

def get_dic_1(texts):
	dic = {}
	prev = "STOP"
	for word in texts:
		if prev in dic:
			if word in dic[prev]:
				dic[prev][word] += 1
			else:
				dic[prev][word] = 1
		else:
			dic[prev] = {}
			dic[prev][word] = 1
		prev = word
	return normal_1(dic)


####################  2-gram picking #####################

def normal_1(dic):
	for i in dic:
		total = 0.0
		for j in dic[i]:
			total += dic[i][j]
		step = 0.0
		for j in dic[i]:
			dic[i][j] = (step, step + (dic[i][j]/total))
			step = dic[i][j][1]
	return dic

		
def get_dic_2(texts):
	dic = {}
	prev_1 = "STOP"
	prev_2 = "STOP"
	for word in texts:
		if prev_1 in dic:
			if prev_2 in dic[prev_1]:
				if word in dic[prev_1][prev_2]:
					dic[prev_1][prev_2][word] += 1
				else:
					dic[prev_1][prev_2][word] = 1
			else:
				dic[prev_1][prev_2] = {}
				dic[prev_1][prev_2][word] = 1
		else:
			dic[prev_1] = {}
			dic[prev_1][prev_2] = {}
			dic[prev_1][prev_2][word] = 1
		prev_1 = prev_2
		prev_2 = word
	return normal_2(dic)

def normal_2(dic):
	for i in dic:
		for j in dic[i]:
			total = 0.0
			for k in dic[i][j]:
				total += dic[i][j][k]
			step = 0.0
			for k in dic[i][j]:
				dic[i][j][k] = (step, step + (dic[i][j][k]/total))
				step = dic[i][j][k][1]
	return dic




		