'''
Homework 2, Exercise 1 and 2
Tyler Schumacher
September 2, 2019
Create the Collatz Sequence while using try and except statement
'''
import sys

def collatz(number):
    #Even Side
    if number % 2 == 0:
      numb = number // 2
    #Odd Side
    elif number % 2 == 1:
      numb = 3 * number + 1
    
    while numb == 1: #When number us 1
      print(numb) #Prints 1
      sys.exit() #Exits program

    while numb != 1: #When number is not 1
      print(numb) #Prints number
      number = numb #Set numb equal to number
      return collatz(number) #Returns number

print('Please give a random number: ') #Asks for a random number
try: #Trys the number
  number = int(input()) #Collects the input
  collatz(number) #Calls collatz
except ValueError: #Catches a value error
  print('Please enter an integer.') #Prints error message
