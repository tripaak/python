user_info = {'name':'akash','age':32}

for items in user_info.items():
   for element in items:
       print (element)


# print(user_info.pop('name'))       
# print(user_info)

# adding data in dict

user_info['companies'] = ['Infosys','Kyriba']

print(user_info)