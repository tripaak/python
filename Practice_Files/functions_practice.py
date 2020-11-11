
# Enter function to take string value and returns last charcter



def return_last_char(String):
    # return String[len(String)-1]
    return String[-1]


def odd_eve(num):  # num is parameter
    if num % 2 == 0:
        return "Even"
    else:
        return "ODD"



#call funstions
#         
number = int (input("Enter any number : "))
print (odd_eve(number))  # number is argument 



