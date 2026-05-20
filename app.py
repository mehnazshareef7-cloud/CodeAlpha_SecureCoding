import getpass

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

stored_password = "Secure@123"

if username == "admin" and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")