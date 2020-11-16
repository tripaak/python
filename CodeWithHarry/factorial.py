# Problem staement : 
# 1. find the factorial of given numbers 
# 2. find the number of trailing zeros



def factorial_finder(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num*factorial_finder(num-1)

def trainlingZeros(num):
    count = 0
    print("in trailing zeros function ")
    print(num%10)
    while(num%10 == 0):
        print("in while loop")
        print(num)
        num = num / 10 
        count = count + 1
    return count



if __name__ == "__main__":
    userInput = int(input("Eneter any number \n"))
    fac = factorial_finder(userInput)
    zero = trainlingZeros(fac)
    print(f"Factorial of {userInput} is : {fac}")
    print(f"Number of trailing zeros in factorial of {userInput} is : {zero}")