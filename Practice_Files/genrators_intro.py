#generators are memory effiecient and good in performance 
# genrators acan be used once not agin and again

def number(num): # in this case 1 to 10 numbers are genrated and stored in memory 
    for i in range(1, num+1):
        print(i)


# number(10)

#genrator 
def number_gen(num): # use of yield creates generator its doesnt created 1 to 10 , it creates 1 and wait of next number request 
    for i in range(1, num+1):
        yield(i)


numbers = list(number_gen(10)) #genrator can be converted to list using list func
print(numbers.__sizeof__)
print(numbers)
# for numbr in number_gen(10):   # here for loop is reqesting generator numbers from 1 to next(num)
#     print(numbr)   
