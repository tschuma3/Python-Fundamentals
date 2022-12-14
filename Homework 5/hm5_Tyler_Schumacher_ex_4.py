'''
Homework 5, Exercise 4
Tyler Schumacher
October 6, 2019
Create a stronger password detector
'''
import re

#Checks uppercase letters
def upperCaseCheck(password):
  if re.search('[A-Z]', password):
    return True
  return False

#Checks lowercase letters
def lowerCaseCheck(password):
  if re.search('[a-z]', password):
    return True
  return False

#Checks digits
def digitCheck(password):
  if re.search('[0-9]', password):
    return True
  return False

#Asks user for a password and checks if the password is strong or weak
password = input("Enter a password: ")
if len(password) >= upperCaseCheck(password) and lowerCaseCheck(password) and digitCheck(password):
  print('This is a strong password!')
else:
  print('This is a weak password!')