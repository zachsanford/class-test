#!/usr/bin/env python3

# This is a cheer program

# Prompt the user for a sports team
userInput = input("Who is your favorite sports team? >> ")

# For Loop to cheer each letter in the name of the team
for letter in userInput:
	cheer = "Gimme a " + letter + "!"
	print(cheer)
	print(letter + "!!")

#After all of the letters are spelled out, "What's that spell??"
print("What's that spell?")
print(userInput + "!!!")
