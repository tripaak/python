# Exercise 2 : Faluty Calculator 
# give wrong answers for below values 
# 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
# input --> 1 operator 2. eneter two numbers 

print("Eneter the operation, *  , + , /")
operator = input()

print("Eneter the first value" )

num1 = int(input())

print("Eneter the first value" )
num2 = int(input())

if operator == '*':
    if num1 == 45 and num2 == 3:
        print(f"Mul of {num1} & {num2} is : 555")
    else:
        print(f"Mul of {num1} & {num2} is : {num1*num2}")    
elif operator == '+' :
    if num1 == 56 and num2 == 9:
        print(f"sum of {num1} & {num2} is : 77")
    else:
        print(f"sum of {num1} & {num2} is : {num1+num2}")
elif operator == '/':
    if num1 == 56 and num2 == 6:
        print(f"Div of {num1} & {num2} is : 4")
    else:
        print(f"Div of {num1} & {num2} is : {num1/num2}")
else:
    print("Wrong operator")        

            