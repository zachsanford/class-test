#!/usr/bin/python3

"""

Functions for PySimpleCalc

"""

"""

    FUNCTIONS

"""

# Menu and user's choice
def menuFunc():
        print("Welcome to PySimpleCalc!")
        print("########################\n\n")
        print("(1) - Add\n")
        print("(2) - Subtract\n")
        print("(3) - Multiply\n")
        print("(4) - Divide\n\n")
        userAnswer = int(input("Please make a selection from the menu >> "))
        return userAnswer
        # test = input()

# First Number
def firstNum():
        userAnswer = int(input("Please enter the first number >> "))
        return userAnswer

# Second Number
def secondNum():
        userAnswer = int(input("Please enter the second number >> "))
        return userAnswer

# Answer
def mathAnswer(x):
        print("The answer is " + str(x))      

# Add
def addFunc(x,y):
        return x + y

# Subtract
def subFunc(x,y):
        return x - y

# Multiply
def multFunc(x,y):
        return x * y

# Divide
def divFunc(x,y):
        return x / y
