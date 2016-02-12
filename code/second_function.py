from subprocess import call


def say_name(a):
	print a
	call(["say", a])

name1 = "pablo"
name2 = "carl"

say_name(name1)
say_name(name2)