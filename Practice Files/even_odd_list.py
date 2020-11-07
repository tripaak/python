
def classify_even_odd(l):
    final = []
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
            #its even 
        else:
            odd.append(i)
            # odd number 
    final.append(even)
    final.append(odd)
    return final

    





number = [1,2,3,4,7,5,6,8,11,9,20,78,21]

print(classify_even_odd(number))