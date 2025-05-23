# Compare two numbers and print which is greater
def greater(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num2 > num1:
        return f"{num2} is greater than {num1}"
    else:
        return "Both numbers are equal"

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
print(greater(n1, n2))