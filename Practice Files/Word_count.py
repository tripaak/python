name = "akash aripathi"
temp = ""
i= 0
while i < len(name):
    if name[i] not in temp:
        print( f"{name[i]} : {name.count(name[i])}" )
        temp += name[i]
    i +=1

print (temp)   