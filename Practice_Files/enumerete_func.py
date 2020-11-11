def func(name,*args):
    # print(names.index('anay'))
    for pos, item in enumerate(args):
        if name == item:
            return pos
    return -1    




name = 'akash1'
names = ['anay','vibha','akash']
print(func(name,*names))


