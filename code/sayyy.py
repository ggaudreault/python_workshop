#!/usr/bin/env python

from subprocess import call
import time

def main():
	#voice = "Daniel"
	voice = "Monica"
	#voice = "Alex"
	#voice = "Zarvox"

	call(["say", "-v", voice, "hello, i am Monica, and it is", time.ctime(), "and I am awake"])
	time.sleep(5)
	call(["say", "-v", voice, "sorry I fell asleep"])
	while(True):
		time.sleep(10)
		call(["say", "-v", voice, "sorry fell asleep again, I am awake now"])


if __name__ == "__main__":
	main()