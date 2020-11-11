#decorator is used to perform certain action before or after the some other function 
import pdb



def dec(func):
    def executor():
        print('Before function run')
        func()
        print("After function run")
    return executor    




def func1():
    print("Hi Akash")    


func1 = dec(func1)   # same as decorator can use @dec above func1

func1()