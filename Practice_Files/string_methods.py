name, char = input("Enter your name and a charcter in comma seprate: ").split(",")

# print("Length of name is "+str(len(name)))

# print ("Count of character is :"+ str(name.count(char)))

#Using string formatting 

print(f"Length of name is {len(name.strip())}")

print (f"count of character is {name.lower().count(char.strip())}")