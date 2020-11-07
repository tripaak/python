name, age = input("Input your name and age comma seperated: ").split(",")
age = int(age)
if name[0].lower() == 'a' and age >= 10:
    print("You can watch coco")

else:
    print("Sorry you can't watvh coco")    