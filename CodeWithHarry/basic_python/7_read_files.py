file = open('akash.txt','r')
# print(file.read())  # read whole file 

# print(file.readline()) # read line 

# for line in file:
#     print(line) # print line by line 


# print(file.readlines())  # store lines in list

for line in file.readlines():
    print(line)     

file.close()    