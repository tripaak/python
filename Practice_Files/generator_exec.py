# create generator 
# it takes number
# and create even numbers from 1 to input number
# for eg. input = 10 , genreated numbers are 2,4,6,8


def generator_even(n):
    for i in range(1,n+1):
        if i%2 == 0:
           yield(i)




#genrator comprehension 

def generator_even_comp(n):
        return (i for i in range(1, n+1) if i%2 == 0)
        
    


for numb in generator_even_comp(5):
    print(numb)