

def adition(n1,n2):
    total = n1 + n2
    return total


def subtraction(n1,n2):
    if n1 > n2:
       total = n1-n2
    else:
        total = n2-n1    
    return total


# print(f"Sum of numbers is: {subtraction(1,5)}") 
# 
number1, number2 = input("Please eneter two numbers, seperated by comma: ").split(',')

#This block convert string to integer

number1 = int(number1)
number2 = int(number2)



operation = input("Input your operation for addition Eneter '+', for subtraction eneter '-': ")

if operation == '+':
    print(f"Sum of numbers is: {adition(number1,number2)}")
else:
    print(f"Subtraction of numbers is: {subtraction(number1,number2)}")    
