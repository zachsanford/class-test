#!/usr/bin/env python3

# Import the Time Module
import time

# Create the function
def sleeper():
	while True:

		# Get the user input
		num = input('How long to wait? >> ')

		# Try and convert it to a float
		try:
			num = float(num)
		except ValueError:
			print('Please enter a number.\n')
			continue

		# Run the time.sleep() command,
		# and show the before and after times
		print('Before: %s' % time.ctime())
		time.sleep(num)
		print('After: %s' % time.ctime())

# Call the function with a Try Block
try:
	sleeper()
except KeyboardInterrupt:
	print('\n\nKeyboard exception received. Exiting...')
	exit()
