'''
Homework 3, Exercise 3
Tyler Schumacher
September 9, 2019
Create a password locker
'''
import sys
import pyperclip
#! python3
#pw.py - An insecure password locker program.
passwords = {'Email' : 'JKL:DF234@#$', 'Twitter' : 'asd;lfjk@#$', 'YouTube' : 'as;ldkjf;sljf234', 'Facebook' : 'jksljlse930kfe0'}

if len(sys.argv) < 2:
  print('Usage: python pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1] #The first command line is the acount name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password ' + account + ' copied to clipboard.')
else:
    print('The account ' + account + ' could not be found')