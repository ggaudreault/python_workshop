import re


### Super small and cute

def clean(text):
	t = text.replace(')', ' ').replace('(', ' ').replace('[', ' ').replace(']', ' ').replace(',', ' ').replace(':', ' ').replace('-', ' ').replace('.', ' STOP ').replace('?', ' STOP ').replace('\n', ' ').replace('/', ' ')
	return "STOP " + t