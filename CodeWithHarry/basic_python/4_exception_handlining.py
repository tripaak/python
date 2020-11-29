num1 = input("Eneter number 1: \n")

num2 = input("Eneter number 2: \n")



# try exception is used to bypass the block of program 
# which is prone to error and catch the error in exception 
# so that the program doesnt stope with error insted keeps going without stopping 


try :
    print("sum of number 1 & 2 is :",int(num1) +int(num2))

except Exception as e:
    print(e)

print("Thnaks for input, Good bye !!")    
