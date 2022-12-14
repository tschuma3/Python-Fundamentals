'''
Homework 3, Exercise 2
Tyler Schumacher
September 9, 2019
Create a game of Tic-Tac-Toe
'''
import random

def draw(board): #This draws the board
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')

def playersInputLetter(): #This asks for what the player wants to be
  letter = ''
  if letter != 'X' or letter != 'O':
    print("Would Player One like to be X or O")
    letter = input().upper()
  if letter == 'X':
    return ['X', 'O']
  else:
    return ['O', 'X']

def firstToGo(): #Which player goes first
  ran = random.randint(0, 1)
  if ran == 0:
    return 'Player One'
  else:
    return 'Player Two'

def moveMaker(board, letter, move): # makes the actual move
  board[move] = letter

def copyOfBoard(board): #Makes a copy of the board
  dupeBoard = []
  for i in board:
    dupeBoard.append(i)
  return dupeBoard

def freeSpace(board, move): #As long as there is a free space
  return board[move] == ' '

def getPlayerOneMove(board): # Player one moves
  move = ''
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
    print("What is the next move")
    move = input()
    return int(move)

def getPlayerTwoMove(board): #Player two moves
  move = ''
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
    print("What is the next move")
    move = input()
    return int(move)

print("Welcome to Tic-Tac-Toe!")

while True:
  theBoard = [' '] * 10
  playerLetterOne, playerLetterTwo = playersInputLetter()
  turn = firstToGo()
  print(turn + ' will go first')
  playingTheGame = True

  while playingTheGame: #When the game is running
    if turn == 'Player One': #Takes care of player one
      draw(theBoard)
      move = getPlayerOneMove(theBoard)
      moveMaker(theBoard, playerLetterOne, move)
    elif turn == 'Player Two': #Takes care of player two
      draw(theBoard)
      move = getPlayerTwoMove(theBoard)
      moveMaker(theBoard, playerLetterTwo, move)