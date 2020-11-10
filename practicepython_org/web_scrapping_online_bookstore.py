import requests
from csv import reader,writer
from bs4 import BeautifulSoup


base_url= "http://books.toscrape.com/"

r = requests.get(base_url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')

books_containers = soup.find_all('article',class_='product_pod') 

with open('books.csv','w',newline='') as csv_file:
    csv_writer = writer(csv_file)
    header = ['link','book_name','price','is_in_stock']
    csv_writer.writerow(header)
    for article in books_containers:
        data= []
        data.append(base_url+article.a.get('href'))
        data.append(article.find('h3').a.get('title'))
        data.append(article.find('p',class_='price_color').text)
        data.append(article.find('p',class_='instock availability').text.strip())
        csv_writer.writerow(data)
    





# print(list(books_containers))

# first_book = books_containers[0]
# # print(first_book)
# first_link = first_book.a.get('href')
# print(first_link)
# first_title = first_book.find('h3').a.get('title')
# print(first_title) # yet to sort out 
# first_price = first_book.find('p',class_='price_color').text
# print(first_price)
# first_book_is_stock = first_book.find('p',class_='instock availability').text.strip()
# print(first_book_is_stock)



# print("-----------Updated code----------")

     


    











    