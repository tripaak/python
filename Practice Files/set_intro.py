##define set

s = {1, 2, 3, 4}

##printing elements 
# for i in s:
#     print(i)


##checking contents
# if 5 in s:
#     print("Present")
# else:
#     print("Not Present")    


## add item in set

# s.add(5)
# print(s)

## Set math operations 
## Unions
## intersections

s1 = {1,2,3,4}
s2 = {3,4,5,6}

union_set = s1 | s2

print(f"Union value is : {union_set}")


intersection_set = s1 & s2

print(f"Intersecion value is : {intersection_set}")
