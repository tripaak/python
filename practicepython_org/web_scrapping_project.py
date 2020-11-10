import requests
from bs4 import BeautifulSoup
from csv import writer

base_url = 'https://www.top500.org/lists/top500/2020/06/'

r = requests.get(base_url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')


## code for CSV file 

filename = 'CoputerTop10.csv'

csv_file= open(filename, 'w')  
csv_writer = writer(csv_file)


# print(soup.find_all('tr'))    

for tr in soup.find_all('tr'):
    data = []
    for th in tr.find_all('th'):
        data.append(th.text)
    if data:
        # print("Inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue 

    for td in tr.find_all("td"):
        # print(td.a)
        if td.a:
            data.append(td.a.text.strip())
        else:
            data.append(td.text.strip())
    # print(data)        
    if data:
        # print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)
        # print(tr.text.strip())