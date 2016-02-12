import math
import time
import random
import clean
import re
import gram
import gen

docs = ["bare_chomsky", "minimalist_pietro", "minimal_hornstein"]
#docs = ["mini_chom"]


def opendocs():
	all_docs = []
	for doc in docs:
		text = open(doc).read()
		ctext = clean.clean(text)
		ctext = re.split(r"[ ]+", ctext)
		all_docs += ctext
	return all_docs

def main():
	texts = opendocs()
	gram.get_count(texts)
	big_dic = gram.get_dic_2(texts)
	print big_dic
	#gen.gibberish_1(big_dic, 200)
	#gen.gibberish_2(big_dic, 200)


if __name__ == "__main__":
	main()




