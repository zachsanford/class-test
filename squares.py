#!/usr/bin/env python3

# For Loop that starts at 5, goes up to 95
# but  instead of going to the next number 
# on each iteration, it skips 10. etc. 5,
# 15,25,35...
for n in range(5, 96, 10):

	# This is an example of string 
	# formatting.
	print('{}*{} = {}'.format(n,n,n**2))
