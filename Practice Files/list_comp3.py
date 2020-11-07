## Execrcise -->
## input list with strings ['abc','def','ijk']
## output ['cba','fed','kji']


#### Using normal method 
# def reverse_strings(input_list):
#     reverse_list = []
#     for item in input_list:
#         reverse_list.append(item[::-1])
#     return reverse_list    

#### Using list comprehension method 
def reverse_strings(input_list):
    reverse_list = [item[::-1] for item in input_list]
    return reverse_list  


print(reverse_strings(['abc','def','ijk']))       
        