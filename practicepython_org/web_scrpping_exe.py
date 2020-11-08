import requests
from bs4 import BeautifulSoup




base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(base_url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

# print(type(soup)) # BeautifulSoup

# print(type(soup.title))  #tag

# print(type(soup.title.string))  #NavigableStrig

# print(soup.find_all('a'))

# print(soup.find('p'))


