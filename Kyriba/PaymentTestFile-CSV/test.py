import random
import time
from csv import writer

ammount_list = []

for i in range(0,10):
    ammount_list.append(random.randrange(1,50000))

print(ammount_list)
print(random.shuffle(ammount_list))    
print(ammount_list)
# with open("output_file.csv",'w',newline='') as op_file:
#     op_writer = writer(op_file,delimiter=";")
#     for i in range(0,1000):
#         op_writer.writerow([random.shuffle(ammount_list)])
