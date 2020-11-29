from datetime import datetime
from csv import DictReader, DictWriter
from csv import reader,writer
import os
import random
import time


# Use Time Stmap for Thirdpart with Prefix 15 cahrcters supported doesnt matter alphabets or numeric


#varibales

os.chdir(r"C:\Users\akash.tripathi\Desktop\python1.0\Kyriba\PaymentTestFile-CSV")

#Create Currency
currency = 'EUR'

#create unique Ammount 1k
ammount_list = []

for i in range(0,1000):
    ammount_list.append(random.randrange(1,50000))

 
# create Thirdparty unique 1k timestamp_random(1,1000)

third_party_list = []

for i in range(0,1000):
    third_party_list.append(str(time.time()).split('.')[0]+'_'+str(random.randrange(0,1000)))

# create Date in format of dd/mm/yyyy
current_date_time = datetime.now()

year = current_date_time.year
month = current_date_time.month
day = current_date_time.day

# print(type(day))
# print(month)
# print(year)
date = str(day)+'/'+str(month)+'/'+str(year)
Refrence = str(current_date_time.timestamp()).split('.')[0]
account_list = []
company_list = []
thirdparty_list = []

with open("Account.csv") as account_file:
    with open("Company.csv") as company_file:        
                accnt_reader = reader(account_file)
                cmpny_reader = reader(company_file)
                for account in accnt_reader:
                    account_list.append(account[0])
                for company in cmpny_reader:
                    company_list.append(company[0])
                


random.shuffle(company_list)
random.shuffle(account_list)
random.shuffle(ammount_list)
random.shuffle(third_party_list)
                
with open("Vibha.csv",'w',newline='') as op_file:
    op_writer = writer(op_file,delimiter=";")
    # for i in range ( 0, 10): ye comment hai 
    for i in range(0,1000):
        op_writer.writerow([company_list[i],account_list[i],date,ammount_list[i],third_party_list[i],'','',currency,'',Refrence])
