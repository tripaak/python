from functools import wraps
import time


def calculate_func_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        returned_val = function(*args, **kwargs)
        t2 = time.time()
        print(f"Total time took for execution of function {function.__name__} is : {t2-t1}")
        return returned_val
    return wrapper    


@calculate_func_time
def add(a,*args):
    print("")
    # print("")
    # print("")
    # print("")
    # print("")
    return [num**a for num in args]



numbers = [1,2,3,4,45,88,96,78,36,855,966,10000000]

print(add(10,*numbers))