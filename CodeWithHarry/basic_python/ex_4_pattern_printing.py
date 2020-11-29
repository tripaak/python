# Excerice: Pattern printing 
#             take integer n , e.g. n=4
#             take boolean 1 or 0 , type cast to True or False 

#             if True
#             *
#             **
#             ***
#             ****

#             if False

#             ****
#             ***
#             **
#             *


def pattern_printing(num,decision):
    if bool(decision) == True:
        for i in range(1,num+1):
            print('* '*i)
    # else:
    #     for i in range(1,num+1):
    #         print('* '*(num+1-i))    

# Another approach below , range method can be used to decrement using step as -1 
    else:
        for i in range(num,0,-1):
            print('* '*(i))           

    
    





pattern_printing(4,0)
