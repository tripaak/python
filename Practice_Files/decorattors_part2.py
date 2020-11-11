from functools import wraps

#decorator is a function that enhance the functionality of other function
# @ sign is used before the function to enhance functionality

def decorator_function(any_function):
    @wraps(any_function)      # required to give details of __name__ & __doc__
    def wrapper_function(*args, **kwargs): #  writes args and kwargs to take arguments
        """ This is wrapper function """   #doc line
        print("this is awsome function")
        return any_function(*args, **kwargs) #  writes args and kwargs to take arguments # use return to get return value
    return wrapper_function    

    

@decorator_function
def func(num):
    print(f"This is Function , which takes arguments {num}")

@decorator_function
def add(a,b):
    """ This is add function """
    return a+b


# print(add(8,9))
# func(7)


print(add.__doc__)

print(add.__name__)
