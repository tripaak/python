## list comprehension

## Create list of square of 1 to 10

def create_list(n):
    # #Using normal method 
    # square_list = []
    # for i in range(1,n+1):
    #     square = i**2
    #     square_list.append(square)
    #     square = 1 
    # return square_list

    #using list comprehension
    square_list = [i**2 for i in range(1,n+1)]
    return square_list



print(create_list(10)) #call function
