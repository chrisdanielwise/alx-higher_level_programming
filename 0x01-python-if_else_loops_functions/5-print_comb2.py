#!/usr/bin/python3

for i in range(00, 100):
	if i <= 10:
		print("{0:02d}".format(i),end=", ")
	elif i == 99:
		print("{:d}".format(i),end="")
	else:
		print("{:d}".format(i),end=", ")
