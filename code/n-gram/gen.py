import random


####################  1-gram generation #####################


def gibberish_1(dic, total):
	step = "STOP"
	text = ""
	index = 0
	while index < total:
		p = random.random()
		for i in dic[step]:
			if dic[step][i][0] < p < dic[step][i][1]:
				if (i == "STOP"): 
					text += "."
				else: text += " " + i
				step = i
				break
		index += 1
	print text


####################  2-gram generation #####################

def gibberish_2(dic, total):
	step_1 = "STOP"
	step_2 = "STOP"
	text = ""
	index = 0
	while index < total:
		p = random.random()
		for i in dic[step_1][step_2]:
			if dic[step_1][step_2][i][0] < p < dic[step_1][step_2][i][1]:
				if (i == "STOP"): 
					text += "."
				else: text += " " + i
				step_1 = step_2
				step_2 = i
				break
		index += 1
	print text
