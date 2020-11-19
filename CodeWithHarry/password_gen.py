import string
import random

password_len = 8

s1 = string.ascii_lowercase

s2= string.ascii_uppercase

s3= string.digits

s4 = string.punctuation

s= list()

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# print("".join(s[0:password_len]))

# print(random.choice(s))
print("your password is : \n")
print("".join(random.sample(s,password_len)))




