#!/usr/bin/env python3

openFile = open('secretpassword.txt')

password = openFile.read().split()


print('Enter your password.')
userInput = input()

if userInput == password[0]:
	print('Access Granted.')

else:
	print('Access Denied.')
