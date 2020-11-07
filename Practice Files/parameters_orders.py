# Order of parameters 
# PADK
# 1. parameters
# 2. *args
# 3. Default parameters
# 4. **kwargs


def func(name, *args, last_name = 'Default' , **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)


func('anay',1,2,3,4,5,last_name='Tripathi',age = 5, gender = 'Male')
