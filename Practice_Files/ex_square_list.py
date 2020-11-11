def square_list(input_list):
    output_list = []
    for i in input_list:
        output_list.append(i**2)
    return output_list


# numbers = [1,2,3,4,5]
numbers = list(range(1,11))
print(square_list(numbers))        
