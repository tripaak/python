#Problem: Bar security will ask your date of birth if your age is above 18 then you are allowed else not allowed 
# Enter date of birth in format DD-MM-YYYY


# string --> "Vibha", "aakash"
# int -->1,2,3
# float --> 5.5, 6.9 
# bool --> True False 

from datetime import datetime
import timedelta
 



def bar_age_check(dob):
    date_of_birth = datetime.strptime(dob,'%d-%m-%Y')
    # print("Your date of Birth is : ",date_of_birth)
    # print(type(date_of_birth))

    today_date = datetime.now()
    # print("Today\'s date is : ",today_date)
    # print(type(today_date))

    your_age_in_days = today_date - date_of_birth
    # print(your_age_in_days)

    # print(your_age_in_days.days)
    

   
    

    your_age = your_age_in_days.days/365
    print("Your Age  is : ",int(your_age))
    if your_age > 18:
        return "You are allowed in Bar"
    else:
        return "Not allowed!! Call security"    




inp = input("Enter Your age is DD-MM-YYYY Format please: \n")


print(bar_age_check(inp))

