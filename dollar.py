#!/usr/bin/env python3

dollar = [' ________________ ','|  _|_  __  _|_  |','| |_|_ /  \|_|_  |','|  _|_|\__/ _|_| |','|___|________|___|']

rows = int(input('x by x. x ='))
cr = '\n'

i = 1
while i <= rows:
	print(cr,rows*dollar[0],cr,rows*dollar[1],cr,rows*dollar[2],cr,rows*dollar[3],cr,rows*dollar[4])
	i += 1
