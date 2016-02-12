# -*- coding: utf-8 -*-
## got info from http://donnees.ville.montreal.qc.ca/dataset

import re

global name
global text

def getL():
	global text
	name_patt = "alexis"
	name_patt2 = "127"
	text = open("Riviere_des_Prairies_Pointe_aux_Trembles_Arbres_publics_2015_12_03.csv", "r").readlines()
	for line in text:
		if re.search(name_patt, line, re.I) and re.search(name_patt2, line, re.I):
			print line.replace("  ", "")

if __name__ == "__main__":
	getL()