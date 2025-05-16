def main():
    temp_f = float(input("Fahrenheit: "))
    temp(temp_f)

def temp(x):
    print(f"{(x - 32) * 5/9:.1f} °C")
    
main()
