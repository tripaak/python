import random


wining_number = random.randint(1,50)

temp_var = True
i = 1

while temp_var:
    guessing_number = int (input(" Enter any number between 1 to 50:"))
    if guessing_number == wining_number:
        print("You win !!")
        print(f"You guessed this number in {i} times ")
        temp_var = False
    elif guessing_number > wining_number:
        print("Too High !!")
       
    else : 
        print("Too Low !!")
    i += 1     