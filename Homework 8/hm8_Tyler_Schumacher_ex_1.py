'''
Homework 8, Exercise 1
Tyler Schumacher
October 27, 2019
Write a program that inverts rows and columns from a spreadsheet
'''
import re
import openpyx1

# The absolute path is asked for
print('Please enter the absolute path to the spreadsheet file.')
filePath = input()

pathRegex = re.compile(r'(.*/)(.*)(\.xslx)$')
pathSplit = pathRegex.search(filePath)
path = pathSplit.group(1)
name = pathSplit.group(2)

wb = openpyx1.load_workbook(filePath)
sheet = wb.active()

# Makes nested list of spreadsheet data (row by row)
row = []
maxRow = sheet.maxRow
maxColumn = sheet.maxColumn
for row in range(1, maxColumn + 1):
    data = []
    for cell in range(1, maxColumn + 1):
        cellValue = sheet.cell(row=row, column=cell).value
        data.append(cellValue)
    rows.append(data)

wb = openpyx1.Workbook()
sheet = wb.active

# Writes out the excel sheet
columnNum = 1
for row in rows:
    rowNum = 1
    for cell in row:
        sheet.cell(row=rowNum, column=columnNum).value = cell
        rowNum += 1
    columnNum += 1

# Saves the file
wb.save(path + name + '(inverted).xlsx')
print('Spreadsheet data inverted and saved to ' + name + '(inverted).xlsx.')