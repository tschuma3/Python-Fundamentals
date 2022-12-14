'''
Homework 2, Exercise 5
Tyler Schumacher
September 2, 2019
Guessing a number
'''
import random

guessesUsed = 0 #Initialized

#Introduction
print('Hello!')
print('You have 7 chances to guess my number.')
print('My number is between 1 and 33')

number = random.randint(1, 33) #Random number between 1 and 33 is chosen
low = 1 #Initialized
high = 33
guess = random.randint(1, 33) #Random guess
while guessesUsed < 7: #While less than 7 guesses
  print('Take a guess!')
  guess = (low + high) // 2 #Takes guess based off previous guess
  print(guess)
  guess = int(guess)

  guessesUsed = guessesUsed + 1

  if guess < number: #Guess is too low
    print('Your guess is too low!')
    low = guess + 1
  elif guess > number: #Guess is too high
    print('Your guess is too high!')
    high = guess
  elif guess == number: #Correct guess
    break

if guess == number: #Correct guess
  guessesUsed = str(guessesUsed) #Converted to string
  number = str(number) #Converted to string
  print('Nice job!')
  print('You guessed ' + number + ' in ' + guessesUsed + ' guesses!')
else: #Did not guess in under 7 guesses
  number = str(number) #Converted to string
  print('You were not able to guess my number in 7 guesses.')
  print('My number was ' + number)
