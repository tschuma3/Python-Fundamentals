'''
Homework 8, Exercise 3
Tyler Schumacher
October 27, 2019
Write a program that calculates and writes another file based on the census data
from 2010
'''
import openpyxl
import pprint

# Read the Spreadsheet
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for state exists
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tract': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

# Open a new file and write the contents of countyData to the file
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('All done!')
