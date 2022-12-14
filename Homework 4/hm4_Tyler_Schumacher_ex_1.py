'''
Homework 4, Exercise 1
Tyler Schumacher
September 29, 2019
Find the area, diagonal, and perimeter of the given shape
'''
import math

#Rectangle
class Rectangle:
  #Calculates the area and prints to 2 decimal places
  def area(self, width, height, radius, sideLength):
    area = width * height
    return print('Your rectangle area is: ' + str(round(area, 2)))
  #Calculates the diagonal and prints to 2 decimal places
  def diagonal(self, width, height, radius, sideLength):
    diagonal = math.sqrt(math.pow(width, 2) + math.pow(height, 2))
    return print('Your rectangle diagonal is: ' + str(round(diagonal, 2)))
  #Calculate the perimeter and prints to 2 decimal places
  def perimeter(self, width, height, radius, sideLength):  
    perimeter = (width * 2) + (height * 2)
    return print('Your rectangle perimeter is: ' + str(round(perimeter, 2)))

class Circle:
  #Calculates the area and prints to 2 decimal places
  def area(self, width, height, radius, sideLength):
    area = math.pow(math.pi * radius, 2)
    return print('Your circle area is: ' + str(round(area, 2)))
  #Calculates the diagonal and prints to 2 decimal places
  def diagonal(self, width, height, radius, sideLength):
    diagonal = radius * 2
    return print('Your circle diagonal is: ' + str(round(diagonal, 2)))
  #Calculate the perimeter and prints to 2 decimal places  
  def perimeter(self, width, height, radius, sideLength):
    perimeter = 2 * math.pi * radius
    return print('Your circle perimeter is: ' + str(round(perimeter, 2)))

class Square:
  #Calculates the area and prints to 2 decimal places
  def area(self, width, height, radius, sideLength):
    area = sideLength * 2
    return print('Your square area is: ' + str(round(area, 2)))
  #Calculates the diagonal and prints to 2 decimal places
  def diagonal(self, width, height, radius, sideLength):
    diagonal = math.sqrt(2) * sideLength
    return print('Your square diagonal is: ' + str(round(diagonal, 2)))
  #Calculate the perimeter and prints to 2 decimal places
  def perimeter(self, width, height, radius, sideLength):  
    perimeter = sideLength * 4
    return print('Your square perimeter is: ' + str(round(perimeter, 2)))

#Asks user for values
print('Please give a width.')
width = float(input())
print ('Please give a height.')
height = float(input())
print('Please give a radius.')
radius = float(input())
print('Please give a side length.')
sideLength = float(input())

#Set classes to variables
rectangle = Rectangle()
circle = Circle()
square = Square()

#Calles the area, diagonal, and perimeter functions
for shape in (rectangle, circle, square):
  shape.area(width, height, radius, sideLength)
  shape.diagonal(width, height, radius, sideLength)
  shape.perimeter(width, height, radius, sideLength)

#Perimeter of a circle with radius that is half of the diagonal of a rectangle with a length 20 and a width 1
print('')
print('Here are your calculations with a width of 20, height of 10, radius of 11.18, and side length of 1.')
width = 20
height = 10
radius = 11.18
sideLength = 1
for shape in (rectangle, circle, square):
  shape.area(width, height, radius, sideLength)
  shape.diagonal(width, height, radius, sideLength)
  shape.perimeter(width, height, radius, sideLength)  