lis = ["Akash","Vibha","Anay"]

dic = {
    "name":"akash",
    "age": "32",
    "surname":"tripathi"
}

# for item in lis:
#     print(item)



# for key,value in dic.items():
    # print(key,value)


tup = (1,2,3,4)

# for item in tup:
    # print(item)



# Quiz : create list with numbers of and type of elements , print if the item is integer and greter than 6     


list_1 = ['akash',32,2,10,'male','anay',5,18,6.3]

for item in list_1:
    if str(item).isnumeric():
    # if type(item) is int:
        if item > 6:
            print(item)
