import requests
from bs4 import BeautifulSoup




base_url = 'https://www.top500.org/lists/top500/2020/06/'

r = requests.get(base_url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

# print(type(soup)) # BeautifulSoup

# print(type(soup.title))  #tag

# print(type(soup.title.string))  #NavigableStrig

# print(soup.find_all('a'))

# print(soup.find('p'))

# print(soup.find_all('p',class_='star-rating Four'))

# print(soup.prettify)

# print(soup.body.findAll(text='Soumission'))  # to find text in soup

# print(soup.find_all('tr'))

# title = soup.title
# print(title)

# print(soup.find_all('tr'))

       