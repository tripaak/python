import requests
from bs4 import BeautifulSoup




base_url = r'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(base_url)

print(r.status_code)
# print(r.text)
print(r.__sizeof__())
print(r.text.find('I don’t know what is'))

# print(r)