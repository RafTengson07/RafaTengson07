while True:
    try:
        age = int(input("Please enter your age: "))
        if 0 <= age <= 120:
            break
        else:
            print("Please re-enter inside the range (0-120)")
    except ValueError:
        print("Invalid age. Please enter a number.")

print(age)