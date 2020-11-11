## Exercise 
## Input = [True, False, 1, 1.5, 3, [1,2,3,5]]
## Output = ['1','1.5','3']  # consider only int and float and store it as string 


Input_list = [True, False, 1, 1.5, 3, [1,2,3,5]] #input list 

#Output_list = []

## normal method
# for item in Input_list:
#     if (type(item) == float or type(item) == int) :
#        Output_list.append(str(item))


## using list comprehension

def num_to_string(Input_list):
    return[str(item)  for item in Input_list if (type(item) == int or type(item) == float)]
    #print(Output_list)




print(num_to_string([True, False, 1, 1.5, 3, [1,2,3,5]]))


