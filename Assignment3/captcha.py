import random

correct_userid = "admin"
correct_password = "1234"

userid = input("Enter user ID:")
password = input("Enter password:")

if userid == correct_userid and password == correct_password:
    captcha = random.randint(1111,9999)

    print("CAPTCHA:",captcha)

    user_input = int(input("Enter the above captcha number:"))

    if user_input == captcha:
        print("Login successfull.")

    else:
        print("captcha did not match Login failed.")
else:
    print("Invalid user ID or password.") 