from functools import wraps

def print_function_data(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print(f' You are calling {any_function.__name__} function')
        print(f'{any_function.__doc__}')
        return any_function(*args, **kwargs)
    return wrapper_function    


@print_function_data
def add(a,b):
    """ This functiona takes 2 parameters and return sum """
    return a+b

@print_function_data
def sub(a,b):
    """ sub dunction doc line """
    if a > b:
        return a-b
    else:
        return b-a    

print(add(10,5))  
print(sub(10,5))  