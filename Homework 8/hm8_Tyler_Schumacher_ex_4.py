'''
Homework 8, Exercise 4
Tyler Schumacher
October 27, 2019
Write a program that fetches the weather for the next three days from a specific
city and prints it out
'''
import json
import requests
import sys

# Get the location from command line argument
if len(sys.argv) < 2:
    print('Usage: hm8_Tyler_Schumacher_ex_4.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON Data
website = 'http://api.openweathermap.org/data/2.5/forcast/daily?q=%s&cnt=3' % location
response = requests.get(website)
response.raise_for_status()

# Loads JSON Data
weatherData = json.load(response.text)

# Prints the weather
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('The Day After Tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
