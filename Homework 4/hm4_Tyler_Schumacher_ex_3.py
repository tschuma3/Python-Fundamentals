'''
Homework 4, Exercise 3
Tyler Schumacher
September 29, 2019
Use generator comprehension expression to find the first 10 pythogorian triplets
'''
#Take function talked about in class
def take(n, seq):
  seq = iter(seq)

  result = []
  try:
    for i in range(n):
      result.append(next(seq))
  except StopIteration:
    pass
  return result  

#Integer function talked about in class
def integers():
  i = 1
  while True:
    yield i
    i = i + 1  

#Pyt function calculates the triplets based off of ranges and the number given
pyt = ((x, y, z) for z in integers() for y in range(1, z) for x in range(1, y) if x*x + y*y == z*z)

#Prints out the triplets and gives a number
print(take(10, pyt))  