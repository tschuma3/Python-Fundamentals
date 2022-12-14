'''
Homework 5, Exercise 1
Tyler Schumacher
October 6, 2019
Slow down a program using decorators
'''
import time
import functools

def slowDown(func):
  @functools.wraps(func)
  def wrapperSlowDown(*args, **kwargs):
    time.sleep(1)
    return func(*args, **kwargs)
  return wrapperSlowDown

@slowDown
def countdown(number):
  if number >= 0:
    print(number)
    countdown(number - 1)
  else:
    print('Whoo!')

number = 10
countdown(number)