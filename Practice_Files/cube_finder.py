# Execercise 
# Define a Function that takes a number 
# return a dictionary containing cubes of number from 1 to n

# example

# cube_finder(3)
# {1:1, 2:8, 3:27}

####### First approach

# def cube_finder(input_number):
#     dNumb = {}
#     for j in range(1,input_number + 1):
#         vCube = 1 
#         for i in range(1,4):
#                 vCube = vCube * j
#         dNumb[j] = vCube
#     return  dNumb  #print(vCube, end=" ")
        
 ####### Second approach   

def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3    # Without using FOR loop
    return cubes    



print(cube_finder(10))