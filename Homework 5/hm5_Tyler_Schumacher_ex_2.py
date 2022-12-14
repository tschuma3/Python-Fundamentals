'''
Homework 5, Exercise 2
Tyler Schumacher
October 6, 2019
Improve the runtime performance of the Fibonacci sequence
'''

def cache(func):
  cache = dict()
  def cacheFunc(*args):
    if args in cache:
      return cache[args]
    result = func(*args)
    cache[args] = result
    return result
  return cacheFunc

@cache
def fibonacci(num):
  if num < 2:
    return num
  return fibonacci(num - 1) + fibonacci(num - 2)

num = 0
print(fibonacci(num))  