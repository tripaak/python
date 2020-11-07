# Remember the rules:

# Rock >> scissors
# Scissors >> paper
# Paper >> rock

user_name_1 = input("Enter your name :")
user_name_2 = input("Eneter your name :")





user1_answer = input(f"Dear {user_name_1}, Choose between Rock, Scissors & Paper :")
user2_answer = input(f"Dear {user_name_2}, Choose between Rock, Scissors & Paper :")


def game(user1_answer,user2_answer):
    if user1_answer == user2_answer:
        print(f"Its a tie between {user_name_1} & {user_name_2}")

    elif user1_answer == 'ROCK' :
        if user2_answer == 'SCISSORS':
           print(f"{user_name_1} Wins !!")
        else:
            print(f"{user_name_2} Wins !!")  

    elif user1_answer == 'SCISSORS' :
        if user2_answer == 'PAPER':
           print(f"{user_name_1} Wins !!")
        else:
            print(f"{user_name_2} Wins !!") 


    elif user1_answer == 'PAPER' :
        if user2_answer == 'ROCK':
           print(f"{user_name_1} Wins !!")
        else:
            print(f"{user_name_2} Wins !!")         




# some comment
game(user1_answer.upper(),user2_answer.upper())

