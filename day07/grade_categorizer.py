# Categorize student's grade based on marks
def grade_category(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks. Must be between 0 and 100."
    elif marks >= 90:
        return "Grade: A"
    elif marks >= 80:
        return "Grade: B"
    elif marks >= 70:
        return "Grade: C"
    elif marks >= 60:
        return "Grade: D"
    else:
        return "Grade: F"

try:
    marks = float(input("Enter your marks (0-100): "))
    print(grade_category(marks))
except ValueError:
    print("Invalid input. Please enter a number.")