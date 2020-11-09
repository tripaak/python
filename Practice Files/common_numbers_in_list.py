num1 = [1,2,8,75,96,89,56,74,23]
num2= [1,96,74,8,6,10]

common = set()

common2 = {1,8}

for i in num1:
    for j in num2:
        if i == j:
            common.add(i)
print(common)            


print(common.intersection(common2))  # to find common numbers is sets 