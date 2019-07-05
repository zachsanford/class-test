#!/usr/bin/python3

"""

A simple calculator written
in Python.

"""

# Import the functions
from CalcFuncs import *
from os import system as s


"""

    CODE

"""

# Clear the CLI
clear = lambda: s('cls')
clear()

# Variables for the user choice switches
userContinue = True
notCorrect = True

# "Would you like to go again?" Switch
while userContinue == True:

    # Wrong menu choice switch
    while notCorrect == True:

        # Display the menu for user input
        userChoice = menuFunc()

        # User chose Add
        if userChoice == 1:

            # Clear the CLI
            clear()

            # Get the user's first number
            userFirst = firstNum()

            # Clear the CLI
            clear()

            # Get the user's second number
            userSecond = secondNum()

            # Clear the CLI
            clear()

            # Use the mathmatical function to get the answer
            userSum = addFunc(userFirst,userSecond)

            # Present the answer to the user
            mathAnswer(userSum)

            # Pause
            input("Press any key to continue... ")

            # Correct menu item, Break out of the menu switch
            notCorrect = False

        # User chose Subtract
        elif userChoice == 2:

            # Clear the CLI
            clear()

            # Get the user's first number
            userFirst = firstNum()

            # Clear the CLI
            clear()

            # Get the user's second number
            userSecond = secondNum()

            # Clear the CLI
            clear()

            # Use the mathmatical function to get the answer
            userSum = subFunc(userFirst,userSecond)

            # Present the answer to the user
            mathAnswer(userSum)

            # Pause
            input("Press any key to continue... ")

            # Correct menu item. Break out of the menu switch
            notCorrect = False

        # User chose Multiply
        elif userChoice == 3:

            # Clear the CLI
            clear()

            # Get the user's first number
            userFirst = firstNum()

            # Clear the CLI
            clear()

            # Get the user's second number
            userSecond = secondNum()

            # Clear the CLI
            clear()

            # Use the mathmatical function to get the answer
            userSum = multFunc(userFirst,userSecond)

            # Present the answer to the user
            mathAnswer(userSum)

            # Pause
            input("Press any key to continue... ")

            # Correct menu item. Break out of the menu switch
            notCorrect = False

        # User chose Divide
        elif userChoice == 4:

            # Clear the CLI
            clear()

            # Get the user's first number
            userFirst = firstNum()

            # Clear the CLI
            clear()

            # Get the user's second number
            userSecond = secondNum()

            # Clear the CLI
            clear()

            # Use the mathmatical function to get the answer
            userSum = divFunc(userFirst,userSecond)

            # Present the answer to the user
            mathAnswer(userSum)

            # Pause
            input("Press any key to continue... ")

            # Correct menu item. Break out of the menu switch
            notCorrect = False

        # User chose poorly
        else:

            # Clear the CLI
            clear()

            # Didn't break the menu switch. Will have to make the menu choice again
            userError = input("ERROR: User Choice Incorrect. Please press any key to retry... ")

    # Back to the "Try Again" Switch

    # Clear the CLI
    clear()
    
    # Prompt user to try again
    userAnswer = input("Would you like to try again (y/n) >> ")

    # User wants to go again
    if userAnswer == 'y' or userAnswer == 'Y':

        # Bool remains the same
        notCorrect = True

        # Clear the CLI
        clear()

    # User does not want to go again
    elif userAnswer == 'n' or userAnswer == 'N':

        # Bool switches and the program ends
        userContinue = False

        # Clear the CLI
        clear()

    # User chose poorly
    else:

        # Clear the CLI
        clear()

        # User will have to retry
        input("ERROR: User Choice Incorrect. Please press any key to retry... ")
