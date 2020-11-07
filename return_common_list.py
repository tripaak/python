def return_common_itms(list1,list2):
    output_list = []
    for i in list1:
        for j in list2:
            if i == j:
                output_list.append(i)
    return output_list



number1 = [1,2,8,9]
number2 = [4,8,9,1,2]


print(return_common_itms(number1,number2))