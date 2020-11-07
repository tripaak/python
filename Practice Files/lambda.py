def is_even(n):
    if n%2 == 0:
        return True
    return False

## Using lambda Expression

is_even2 = lambda n : n%2 == 0

print(is_even(5))

print(is_even2(5))
