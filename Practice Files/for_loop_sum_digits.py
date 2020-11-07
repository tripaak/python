# number_input = input("Enter any digit number: ")

# total = 0 

# for i in range (len(number_input)):
#     total = total + int(number_input[i])


# print (total)    



# Check number of characters 


name = "akash tripathi"

temp = ""

for i in range(len(name)):
    if name[i] not in temp:
        print (f"{name[i]}:{name.count(name[i])}")
        temp = temp + name[i]



 #also ceck break & continue        


