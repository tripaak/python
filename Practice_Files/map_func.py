
def is_even(a):
    return a%2 == 0



numbers = [1,2,8,6,9,7,3]


#map function 

is_even_list = map(is_even, numbers)  #map function allows to send entire list to function
for i in is_even_list:
    print(i)

# print(is_even_list)

#filter function 

evens = list (filter(is_even, numbers))

new_evens = list(filter(lambda a:a%2 == 0, numbers))

print(new_evens)

print(evens)