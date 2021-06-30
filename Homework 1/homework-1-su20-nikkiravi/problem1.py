#!/usr/bin/python3
year=2020
# Your code should be below this line
if(not year % 4):
	if(not year % 100):
		if(not year % 400):
			print(True)
		else:
			print(False)
	else:
		print(True)
else:
	print(False)