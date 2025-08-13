import re

while True:
    username = input("Please enter your username: ")
    pattern = r"^[a-zA-Z0-9_]{3,20}$"
    email = input("Please enter your email: ")  
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if not re.match(email_pattern, email):
        print("Invalid email format. Please try again.")
        break
    else:
        password = input("Please enter your password: ")
        pattern2 = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        if not re.match(pattern, username):
            print("Invalid username. It must be 3-20 characters long and can only contain letters, numbers, and underscores.")
            continue

        if not (re.match(pattern2, password) and len(password) >= 8):
            print("Invalid password. It must be at least 8 characters long and contain at least one letter and one number.")
            continue

        print("Sign up successful!")
        break