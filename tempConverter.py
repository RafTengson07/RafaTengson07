value = float(input("Enter a value"))
temp =  input("Enter the temperature")

if temp == 'C' or temp == 'c':
    converted_value = (value * 9/5) + 32
    print(f"{value}°C is {converted_value}°F")
elif temp == 'F' or temp == 'f':
    converted_value = (value - 32) * 5/9
    print(f"{value}°F is {converted_value}°C")
else:
    print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
