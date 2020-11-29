# break --> to exit loop
# continue --> ignore commands below continue and carry on with loop

# Quiz: write a program which take sinput from user indefinity and print "you are winner" if number > 100 

while True:
    print("Enter any number : ")
    num = int(input())
    if num < 100 :
        print("Try Again")
        continue
    else :
        print("You are Winner ")
        break