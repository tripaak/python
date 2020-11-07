from csv import DictWriter

with open('output.csv','w',newline='') as df:
    file_writer = DictWriter(df,fieldnames=['name','surname','age'])
    file_writer.writeheader()
    # file_writer.writerow({'name':'Akash',
    #                       'surname':'Tripathi',
    #                       'age': 32}) # takes dict

    file_writer.writerows([
        {'name':'Akash','surname':'Tripathi','age': 32},
        {'name':'Anay','surname':'Tripathi','age': 5},
        {'name':'Vibha','surname':'Tripathi','age': 32},
        ]) # takes rows of dict 