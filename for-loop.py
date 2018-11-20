#!/usr/bin/env python3

iterations = ["first","second","third","fourth"]
userResult = 0

for x in range(0, 4):
  userInput = int(input('Please enter the ' + iterations[x] + ' number >> '))
  userResult += userInput

print (userResult)
