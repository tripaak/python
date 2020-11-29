import random
# select any number as win number e.g. n = 55
# number of try = 5 
# ask user to eneter any number & print number of guesses left 
# print if enetered number is less or more than n
# print you are winner if guessed right 


win_number = random.randrange(20,80)
# print(win_number)
num_of_try = 5 

while True:
    if num_of_try > 0:
        print(f"You have {num_of_try} guess left")
        user_guess_num = int(input("Guess the number : \n"))
        if user_guess_num > win_number :
            print("To high")
            num_of_try = num_of_try-1
            continue
        elif user_guess_num < win_number:
            print("To less ")
            num_of_try = num_of_try-1
            continue
        elif user_guess_num == win_number:
            print("Guess is right ")
            num_of_try = num_of_try-1
            break
    else:
        print("You have exhausted your chances, Result was ",win_number)
        break        
    
