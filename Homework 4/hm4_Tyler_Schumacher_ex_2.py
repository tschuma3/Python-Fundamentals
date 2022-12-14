'''
Homework 4, Exercise 2
Tyler Schumacher
September 29, 2019
Take a list and reverse it
'''
#Reverse the list
def reverseIter(itReverse):
  for item in reversed(itReverse):
    print(item) 

#The original list to reverse
itReverse = reverseIter([0, 1, 2, 3, 4, 5, 6, 7])

#Prints the list in reverse order
print(type(itReverse))
print(next(itReverse))