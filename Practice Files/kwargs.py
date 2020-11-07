


def details(**kwargs):   #kwargs takes input as dictionary 
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")



details(name = 'Akash', Last_name = 'Tripathi', age = 32 )
