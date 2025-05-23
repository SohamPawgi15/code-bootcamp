# Check if username and password match
def login_check(username, password):
    correct_username = "admin"
    correct_password = "1234"
    username = username.strip().lower()
    password = password.strip()
    return username == correct_username and password == correct_password

user = input("Enter username: ")
pwd = input("Enter password: ")

if login_check(user, pwd):
    print("Login success")
else:
    print("Access denied")