'''
Homework 2, Exercise 3
Tyler Schumacher
September 2, 2019
Work with Comma code
'''
stuff = [] #List created
while True:
  print('Enter a random object' + str(len(stuff) + 1) + 'Or enter nothing to exit the program.') #Asks for a random amount of objects
  things = input() #Collects imput
  if things == '': #If there is no input
    break
  stuff = stuff + [things] #Adds to the stuff list

#Prints objects
print('Your random objects are: ')
for things in stuff:
  print(things, end=", ") #Formats the printed list and prints that list
