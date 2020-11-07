user_input = input("Enter any digit number: ")

input_length = len(user_input)

# print (input_length)
i = 0
total = 0
while i < input_length:
    total = total + int(user_input[i])
    i +=1


print (f"Sum total of entered number is :{total}")    
