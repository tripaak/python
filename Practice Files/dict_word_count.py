

#name = "akash Tripathi"

def word_counter(name):
    #temp = ""
    mydict = {}
    for i in range(len(name)):
       # if name[i] not in temp:
            #print(f"{name[i]}: {name.count(name[i])}")
            mydict[name[i]] = name.count(name[i])
           # temp = temp + name[i]
    print(mydict)        


word_counter("akash_tripathi")
