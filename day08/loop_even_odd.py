# Enter numbers; print each as even or odd
nums = input("Enter numbers separated by commas: ").split(",")
for num in nums:
    n = int(num.strip())
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")