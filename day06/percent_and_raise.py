# Calculate percentage and salary raise
def percent(x, y):
    return round(x / y * 100, 1)

def calc_raise(salary, pct):
    return round(salary * (1 + pct / 100), 2)

print(f"Percent: {percent(20, 40)}%")
salary = float(input("Enter your salary: "))
pct = float(input("Enter raise percent: "))
print(f"New salary: ${calc_raise(salary, pct):.2f}")