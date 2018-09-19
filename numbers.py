#!/usr/bin/env python3

max = -9999999

number = int(input("Enter a number or -1 to stop: "))

while number != -1:
	if number > max:
		max = number
	number = int(input("Enter a number or -1 to stop: "))
print("The largest number is %d" % (max))
