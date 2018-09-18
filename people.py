#!/usr/bin/env python3

# Author: Zachary Sanford (@zachsanford)
# Published: September 18th, 2018

import os

os.system("clear")

class Person:

	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

	def getAddress(self):
		return self.address

userName = input("What is your name >> ")
os.system("clear")
userAge = input("What is your age >> ")
os.system("clear")
userAddress = input("What is your address >> ")
os.system("clear")

user = Person(userName, userAge, userAddress)

userContinue = True

while userContinue == True:
	userChoice = input("Would you like to see your NAME, AGE, ADDRESS, or QUIT (n,a,d,q) >> ")
	os.system("clear")

	if userChoice == 'n':
		print("Your name is", user.getName())
		input()
		os.system("clear")
	elif userChoice == 'a':
		print("You are", user.getAge(), "(s) old.")
		input()
		os.system("clear")
	elif userChoice == 'd':
		print("Your address is", user.getAddress())
		input()
		os.system("clear")
	elif userChoice == 'q':
		print("Goodbye...")
		input()
		os.system("clear")
		userContinue = False
	else:
		print("Please try again.")
		input()
		os.system("clear")
