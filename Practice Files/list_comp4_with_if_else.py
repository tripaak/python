## Execrise 
## list of numbers from 1 to 10
## create op with two list 1. even list 2. odd list


numbers = list(range(1,11))
print(f"List of numbers are : {numbers}")

even_list = []
odd_list = []

## Normal Method 
# for number in numbers:
#     if number % 2 == 0:
#         even_list.append(number)
#     else:
#         odd_list.append(number)
# print(f"Evene numbers are: {even_list}")
# print(f"Odd numbers are : {odd_list}")            


## List comprehension with if else 
even_list = [number for number in numbers if number%2 == 0]
odd_list = [number for number in numbers if number%2 != 0]
print(f"Evene numbers are: {even_list}")
print(f"Odd numbers are : {odd_list}")   
