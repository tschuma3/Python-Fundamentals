'''
Homework 5, Exercise 3
Tyler Schumacher
October 6, 2019
Extract phone numbers and emails and print just the phone numbers and emails
'''
import re  
import pyperclip

#Collects the emails and names
stri = pyperclip.copy('')

#Finds the emails
lis = re.findall('\S+@\S+', stri)

#Prints the emails
print(lis)

#Pastes to pyperclips
pyperclip.paste()