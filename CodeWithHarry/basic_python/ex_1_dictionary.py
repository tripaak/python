# create a dictionary for 4 words and meaning , ask user to input any word and print meaning of this word 

my_dict = {
    "Aller":"To Go",
    "Venir":"To come",
    "Avoir":"To have",
    "Etre":"To be "
}


user_inp = input("Enter any french word to find meaning in english: ")

if my_dict.get(user_inp) is not None:
    print(f"Meaning of {user_inp} is : {my_dict.get(user_inp)}")
else:
    print("Entered word is not present in dict")

