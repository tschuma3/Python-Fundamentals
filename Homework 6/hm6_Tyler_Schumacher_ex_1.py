'''
Homework 6, Exercise 1
Tyler Schumacher
October 13, 2019
This program keeps track of multiple pieces of text
'''
import pyperclip, shelve, sys, pprint

with shelve.open('mcb') as mcbShelf:
  if len(sys.argv) == 3:
    keyword = sys.argv[2]
    #Saves to the clipboard
    if sys.argv[1].lower() == 'save':
      # don't use "all" key cause it has spec meaning
      if keyword.lower() == 'all':
        print("'all' has special meaning. Don't use it as keyword.")
        sys.exit()
      else:
        clipBoard = pyperclip.paste()
        mcbShelf[keyword] = clipBoard
    #Deletes the clipboard content
    elif sys.argv[1].lower() == 'delete':
      #Deletes all keywords
      if keyword.lower() == 'all':
        for keyword in list(mcbShelf.keywords()):
          del mcbShelf[keyword]
      #Deletes specific keywords
      elif keyword.lower() in list(mcbShelf.keywords()):
        del mcbShelf[keyword]
      else:
        print('There is not such a keyword %s' % keyword)
  elif len(sys.argv) == 2:
    #Loads all the keywords to the clipboard
    if sys.argv[1].lower() == 'list':
      keywords = list(mcbShelf.keywords())
      pprint.pprint(keywords)
    #List all the keywords and loads the content.
    elif sys.argv[1].lower() in mcbShelf:
      keyword = sys.argv[1]
      pyperclip.copy(mcbShelf[keyword])
mcbShelf.close()
