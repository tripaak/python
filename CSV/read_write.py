

from csv import  DictWriter,DictReader

with open('read1.csv','r') as rf:
    with open('write.csv','w',newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['name','last_name','age'])
        # csv_writer = DictWriter(wf, fieldnames=['name','surname','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            # csv_writer.writerow(row)
            csv_writer.writerow({
            'name': row['name'],
            'last_name': row['surname'],
            'age': row['age']
            })
