# #Excercise 
# # input num, *nums (list or touple)
# # return list with power num
# #Examle to_power(3,[1,2,3])
# # output list [1**3, 8, 27]
# # Use list comprehension

def to_power(num, *args):
    print(num)
    print(args)
    if not args:
       return "Hey You did not enetered args in input"
    else:    
       return[numbers**num for numbers in args]


nums = [1,2,3,4]

print(to_power(3,*nums))

