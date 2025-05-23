# Check whether a number is even or odd
def even_odd(number):
    return number % 2

n = int(input("Enter a number: "))
if even_odd(n) == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")