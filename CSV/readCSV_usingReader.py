from csv import reader

with open('read1.csv','r') as csv_file:
    csv_reader = reader(csv_file)
    # user_details = ()
    next(csv_reader)
    for row in list(csv_reader):
        print(row)
    # print(user_details)    
