'''
Homework 2, Execise 4
Tyler Schumacher
September 2, 2019
Creating a picture from a grid
'''
grid = [['.', '.', '.', '.', '.', '.'],['.', 'O', 'O', '.', '.', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['O', 'O', 'O', 'O', 'O', '.'], ['.', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['.', 'O', 'O', '.', '.', '.'],  ['.', '.', '.', '.', '.', '.']]

#Row 0
row = ''
for r in range(len(grid)): #For r in the range of row 0's grid length
  row += str(grid[r][0]) #Puts that value in row

#Row 1
row1 = '\n'
for r in range(len(grid)):
  row1 += str(grid[r][1])

#Row 2
row2 = '\n'
for r in range(len(grid)):
  row2 += str(grid[r][2])

#Row 3
row3 = '\n'
for r in range(len(grid)):
  row3 += str(grid[r][3])

#Row 4
row4 = '\n'
for r in range(len(grid)):
  row4 += str(grid[r][4])

#Row 5
row5 = '\n'
for r in range(len(grid)):
  row5 += str(grid[r][5])

#Prints the rows
print(row, row1, row2, row3, row4, row5) 
