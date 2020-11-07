# def reverse_list(input_list):
#     # return input_list[::-1]
#    input_list.reverse()
#    return input_list


def reverse_list(num):
    num1 = []
    for i in range(len(num)):
    #    popped_number = num.pop()
       num1.append(num.pop())
    return num1   








numbers = list(range(1,11))
print(reverse_list(numbers))


