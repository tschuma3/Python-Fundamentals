'''
Homework 6, Exercise 4
Tyler Schumacher
October 13, 2019
Delete any unwanted files that are larger than a certain file size
'''
import os

#Unwanted Files
def unwantedFiles(folder):
  folder = os.path.abspath(folder)

  #Walks through the file tree to see if there are any files larger then a select amount
  for foldername, subfolder, filenames in os.walk(folder):
    for filename in filenames:
      fileSize = os.path.getsize(foldername + '\\' + filename)
      if int(fileSize) < 100000000:
        continue
        os.unlink(filename)
      print('Deleting ' + filename + '...')
unwantedFiles('C:\\User')
print('Done!')