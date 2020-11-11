## Execrise input data from user and store in dict
## Print dictionary in order 

#sample

# name = input("Eneter your name: ")
# Age = int(input("Eneter Your age: "))
# fav_movies = input("Eneter Fav movies: ").split(',')
# fav_music = input("Eneter Fav music: ").split(',')

# users = {}
# users['name'] = name
# users['Age'] = Age
# users['fav_movies'] = fav_movies
# users['fav_music'] = fav_music

#print(users.items())
# for key in users:
#     print(f"{key}:{users[key]}")

### Another option useing .items() method --> This method convert doctionary into list 
# for key, value in users.items():
#     print(f"{key} : {value}")

## to print all keys in dictionary

users = {'name' : 'satish',
'Age' : 55,
'fav_movies' : ['ladla'],
'fav_music' : ['songs']}

# for i in users:
#     print(i)



## to print all values in dictionary

# for i in users.values():
#     print(i)

## get method 
# print(users.get('names'))


## pop 
# print(users.pop('name'))

## popitem

# print(users.popitem())