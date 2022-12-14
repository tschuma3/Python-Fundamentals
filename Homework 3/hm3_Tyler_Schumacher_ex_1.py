'''
Homework 3, Exercise 1
Tyler Schumacher
September 9, 2019
Develop a program that counts the number of occurrences of each letter in a string
'''
import pprint
diLetters = {}
letters = "It was a bright cold day in April, and the clocks were striking thirteen."

print(letters)

#counts = letters

for j in letters:
    if j in diLetters.keys():
        diLetters[j] += 1
    else:
        diLetters[j]=1

pprint.pprint(diLetters)
