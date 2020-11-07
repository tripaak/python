a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def even_list(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list        

def even_list1(numbers):
    even_list1 = [num for num in numbers if num % 2 == 0]
    return even_list1
  





print(even_list1(a))