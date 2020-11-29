def is_armstrong_num(num):
    total = 0 
    for digit in str(num):
        total +=pow(int(digit),3)
    return True if total == num else False 

def gen_armstrong_num(end_limit):
    armstrong_num = []
    for num in range (0,end_limit):
        total = 0
        for digit in str(num):
            total += pow(int(digit),3)
        if total == num:
            armstrong_num.append(total)   
    return armstrong_num         



print(is_armstrong_num(407))

# for item in gen_armstrong_num(1000):
#     print(item)

# print(pow(9,3) + pow(4,3) + pow(7,3) + pow(4,3) )