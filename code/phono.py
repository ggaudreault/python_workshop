#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
import re

global text
global rule

def parse_rule(possible_rule):
	global rule
	match = re.match(r'.*->.*/.*_.*', possible_rule)
	if match:
		match = match.group()
		rule = [re.sub(r'->.*$', "", match), re.sub(r'/.*$', "", re.sub(r'^.*->', "", match)), re.sub(r'_.*$', "", re.sub(r'^.*/', "", match)), re.sub(r'^.*_', "", match)]
	else:
		print "how about you put the rule in the right form and try again"
		ask_rule()

def ask_total():
	ask_text()
	#ask_rule()
	#parse_rule("a->b/_b")
	parse_rule("s->ssss/_")
	#parse_rule("s->z/_")

def ask_rule():
	possible_rule = raw_input("Gimme a phonological rule in form: a->b/c_d: ")
	parse_rule(possible_rule)

def ask_text():
	global text
	#text = "he tabs the blue dogs but not the green dogs"
	#text = "abbababaababba"
	text = "Ce fut un grand Vaisseau taillé dans l'or massif:\nSes mâts touchaient l'azur, sur des mers inconnues;\nLa Cyprine d'amour, cheveux épars, chairs nues,\nS'étalait à sa proue, au soleil excessif.\nMais il vint une nuit frapper le grand écueil\nDans l'Océan trompeur où chantait la Sirène,\nEt le naufrage horrible inclina sa catène\nAux profondeurs du Gouffre, immuable cercueil.\nCe fut un Vaisseau d'Or, dont les flancs diaphanes\nRévélaient des trésors que les marins profanes,\nDégoût, Haine et Névrose, entre eux ont disputés.\nQue reste-t-il de lui dans la tempête brève ?\nQu'est devenu mon coeur, navire déserté?\nHélas! Il a sombré dans l'abîme du Rêve!"
	#text = raw_input("Gimme a string of text: ")
	#text = "Rappers, I monkey flip 'em with the funky rhythm I be kickin'\nMusician, inflictin' composition of pain\nI'm like Scarface sniffin' cocaine\nHolding an M16, see with the pen I'm extreme, now\nBullet holes left in my peepholes\nI'm suited up in street clothes, hand me a nine and I'll defeat foes\nY'all know my steelo with or without the airplay\nI keep some EandJ, sitting bent up in the stairway\nOr either on the corner betting Grants with the cee-lo champs\nLaughing at baseheads tryna sell some broken amps\nG-packs get off quick, forever niggas talk shit\nReminiscing about the last time the Task Horse flipped\nNiggas be running through the block shootin'\nTime to start the revolution, catch a body, head for Houston\nOnce they caught us off-guard, the Mac-10 was in the grass and\nI ran like a cheetah with thoughts of an assassin\nPick the Mac up, told brothers, 'Back up,'' the Mac spit\nLead was hittin' niggas, one ran – I made him backflip\nHeard a few chicks scream, my arm shook, couldn't look\nGave another squeeze, heard it click, 'Yo, my shit is stuck'\nTry to cock it, it wouldn't shoot, now I'm in danger\nFinally pulled it back and saw three bullets caught up in the chamber\nSo now I'm jetting to the building lobby\nAnd it was full of children probably couldn't see as high as I be\n(So what you sayin'?) It's like the game ain't the same\nGot younger niggas pulling the triggers bringing fame to their name\nAnd claim some corners, crews without guns are goners\nIn broad daylight, stickup kids – they run up on us\n45's and gauges, Macs, in fact\nSame niggas will catch you back-to-back, snatching your cracks in black\nThere was a snitch on the block getting niggas knocked\nSo hold your stash 'til the coke price drop\nI know this crackhead who said she's got to smoke nice rock\nAnd if it's good, she'll bring you customers in measuring pots\nBut yo, you gotta slide on a vacation, inside information\nKeeps large niggas erasin' and their wives basin'\nIt drops deep as it does in my breath\nI never sleep, cause sleep is the cousin of death\nBeyond the walls of intelligence, life is defined\nI think of crime when I'm in a New York state of mind"
	
def run_rule():
	print rule
	condition = re.compile(rule[2] + rule[0] + rule[3])
	result = rule[2] + rule[1] + rule[3]
	final_string = re.sub(condition, result, text)
	print "Initial string: " + text + "\nFinal string: " + final_string

def arg_text(arg):
	global text
	text = arg

def main():
	if len(argv) != 3:
		ask_total()
	else:
		arg_text(argv[1])
		parse_rule(argv[2])
	run_rule()

if __name__ == "__main__":
	main()