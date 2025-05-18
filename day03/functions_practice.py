def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

def percent (x,y):
    return round (x / y * 100, 1)
    
def calc_raise(salary, pct):
    return round(salary * (1 + pct / 100), 2)
    
if __name__ == "__main__":
    hello()
    print(f"Percent: {percent(20, 40)}%")
    salary = float(input("Enter your salary: "))
    pct = float(input("Enter raise percent: "))
    new_salary = calc_raise(salary, pct)
    print(f"New salary: ${new_salary:.2f}")
