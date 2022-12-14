'''
Homework 7, Exercise 4
Tyler Schumacher
October 20, 2019
This program sends out multiple reminders to different cities of the weather
'''
import requests

#Gets the website
def weatherWebsite(query):
  res = requests.get('http://weather.gov')
  return res.json

#Prints out the weather based on the city
def weatherPrint(result, city):
  print("{}'s temperature: {} degrees".format(city, result['main']['temp']))
  print("Wind speed: {} mph".format(result['wind']['speed']))
  print("Weather: {}".format(result['wather'][0]['main']))

#Asks what city the weather should be based off of
def main():
  city = input('Please enter a city: ')
  print()
  try:
    query = 'q = ' + city;
    weatherData = weatherWebsite(query);
    weatherPrint(weatherData, city)
    print()
  except:
    print('City name is not found!')

#Check if _name_ is equal to _main_
if __name__ == '_main_':
  main()
