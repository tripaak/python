
def is_palindrome(name):
    if name == name[::-1]:
        return "String is palindrome"
    else:
        return "String is not palindrom"


print(is_palindrome("akash"))
print(is_palindrome("naman"))