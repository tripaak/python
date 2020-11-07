

def func(*args, **kwargs):
    output_list = []
    if kwargs.get('reverse_string') == True:
       for item in args:
        output_list.append(item[::-1].title())
    else:
        for item in args:
            output_list.append(item.title())
    return output_list        

  


names = ['akash','tripathi']

print(func(*names ,reverse_string = True ))