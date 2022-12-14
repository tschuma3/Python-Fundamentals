'''
Homework 7, Exercise 3
Tyler Schumacher
October 20, 2019
This program runs just before you wake up in the morning and checks the weather
'''
import requests, bs4, datetime, time

#Checks if the weather is rainy from www.weather.gov and returns true if rainy at a certain time of the day
def run(self):
  delta = datetime.timedelta(days = 1, hours = 7, minutes = 0)
  while delta == True:
    time.sleep(1)
    def checkWeather():
      website = 'https://weather.gov'
      res = requests.get(website)
      res.raise_for_status()
      soup = bs4.BeautifulSoup(res.text, 'lxml')
      weatherType = soup.select('#styles-xz0ANuU3_nowBlurb_17gst')
      weather = weatherType[0].getText()

      if 'rain' in weather.lower():
        return True
    return checkWeather

#Prints a message based off of checkWeather()
if run:
  print('Take an umbrella and coat today.')
else:
  print('Today will be gorgeous! Enjoy the day!')
