def reverse_string(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[::-1])
    return  output_list   
    


send_list = ['ABC','EFG','IJK']

print(reverse_string(send_list))    