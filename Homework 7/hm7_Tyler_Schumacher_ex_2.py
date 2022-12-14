'''
Homework 7, Exercise 2
Tyler Schumacher
October 20, 2019
This program goes to a image website, selects a specific category, and then downloads the image
'''
import requests, urllib.request
from bs4 import BeautifulSoup

#Asks what wants to be searched and finds the website
category = input("What would you like to search? ").replace(' ', '+')
website = "http://imgur.com/search/score?=" + category
soup = BeautifulSoup(urllib.request.urlopen(website).read(), 'html.parser')
count = 0

#Locates the picture, downloads the picture, and closes the program
for website in soup.find_all('img'):
  picture = website.get('scr')[2:]
  if picture[0] == 'j':
    count += 1
    picture = 'http://' + picture
    g = open('{0}.jpg'.format(count),'wb')
    g.write(requests.get(picture).content)
    g.close() 