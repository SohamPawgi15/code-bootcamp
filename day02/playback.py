def main():
    sen = input("Enter a string: ")
    print(slow(sen))

def slow(x):
    return x.replace(" ", "...")

main()