file = open('akash.txt','r')
# print(file.read())  # read whole file 

# print(file.readline()) # read line 

# for line in file:
#     print(line) # print line by line 

file.tell()   # tell the about the file pointer

file.seek(10) # reset file pointer to charcter 10 
# print(file.readlines())  # store lines in list

for line in file.readlines():
    print(line)     

file.close()    


