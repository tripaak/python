
#decorator is a function that enhance the functionality of other function
# @ sign is used before the function to enhance functionality

def decorator_function(any_function):
    def wrapper_function():
        print("this is awsome function")
        any_function()
    return wrapper_function    

    

@decorator_function
def func1():
    print("This is Function 1")



def func2():
    print("This is Function 2") 



func1()