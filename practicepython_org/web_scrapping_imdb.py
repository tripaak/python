# import urllib2
from bs4 import BeautifulSoup
from requests import get

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
# type(html_soup)
movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')

# print(type(movie_containers))

print(list(movie_containers))

first_movie = movie_containers[0]

# print(first_movie)

first_title = first_movie.h3.a.text
print(first_title)

first_year = first_movie.h3.find('span', class_='lister-item-year text-muted unbold')
first_year = first_year.text
print (first_year)

first_imdb = float(first_movie.strong.text)
print (first_imdb)

# !!!! problem zone ---------------------------------------------
first_description = first_movie.find_all('p', {"class":"text-muted"})[1].text.strip()
# first_description = first_description.text
print(first_description)