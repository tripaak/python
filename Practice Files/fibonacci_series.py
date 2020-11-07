# create fibonacchi series for n numbers 

def fibonacci_series(n):   #user defined funcion 
    a = 0
    b = 1
    if n == 1:
        print(a, end=" ")
    elif n == 2:
        print(a,b,end=" ")  

    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print (c, end=" ")    


fibonacci_series(1)              

