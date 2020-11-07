# execrcise 
# names = ['Akash','Vibha','Om']
# new_list = ['A','V','O']



names = ['Akash','Vibha','Om']
#print(names[0])
# new_list = []
# for val in names:
#     new_list.append(val[0])
# print(new_list)    

## using list comprehension

new_list= [val[0] for val in names]
print(new_list)  