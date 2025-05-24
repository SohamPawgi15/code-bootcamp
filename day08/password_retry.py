# Keep asking for password until correct
correct_password = "open123"
while True:
    entry = input("Enter password: ").strip()
    if entry == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")