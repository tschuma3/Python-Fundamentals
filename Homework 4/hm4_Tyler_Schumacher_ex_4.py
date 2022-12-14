'''
Homework 4, Exercise 4
Tyler Schumacher
September 29, 2019
The generator version of range
'''
from sys import getsizeof

#Creates the generator based off of range
def generator():
  for x in range(100):
    yield x

#Prints the values
print('Values in the range are: ')
for values in generator():
  print(values)

#Prints the size of range and generator
print('')
print('The size of the range is: ')
print(getsizeof(range(100)))
print('The size of the generator is: ')
print(getsizeof(generator))