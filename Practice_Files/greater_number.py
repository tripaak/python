

# program to return grater number 


def grater_num(num1,num2):
    if num1 > num2 :
        return num1 
    else :
        return num2

numb1, numb2 = input("Enter two numbers seprated by comma").split(",")

greater_number = grater_num(int(numb1), int(numb2))

print (f"The greater number from {numb1} & {numb2} is : {greater_number}")