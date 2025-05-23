# Calculate BMI using weight and height
def bmi(weight, height):
    return round(weight / (height ** 2), 2)

w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))

print(f"Your BMI is: {bmi(w, h)}")