# closest power to 2: find number greter than or equal to n whose submission make closest number to power of 2  

# input = 3 
# output = 5 because 3 + 5 = 8 = 2 power to 3 

# 3 --> 3 + 4 --> 7 check if mod with 2 is 0 --> if yes return 4 else --> 3 + 5 --> check 8 % 2 == 0

def closestPowerToTwo(n):
    closest_num = n + 1 
     for i in range(0,n+1):

         x = pow(2, i) 
         if x < closest_num:
            continue
         else:
            closest_num += 1  
        

            
    

print(closestPowerToTwo(5))