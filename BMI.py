# BMI Checker

# BMI Constant
UNDER = 18.5
NORMAL = 24.9
OVER = 29.9

# Pangwe-welcome kay user
print("Mabuhay, ang BMI checker ay nandito na!")

# Tagatanggap ng mga input mula sa user
name = input("Ilagay ang iyong pangalan: ") 
weight = float(input("Ilagay ang iyong timbang (kg): "))
height = float(input("Ilagay ang iyong taas (m): "))
height = height / 100  # Convert cm to m if needed

if (height > 0 and weight > 0):
    bmi = weight / (height ** 2)
    if bmi < UNDER:
        category = "Underweight"
    elif bmi <= NORMAL:
        category = "Normal weight"
    elif bmi <= OVER:
        category = "Overweight"
    else:
        category = "Obese"
    print (f"Hello {name}, ang iyong BMI ay: {bmi:.2f} at ikaw ay {category}.")
else:
    print("Ang timbang mo ay saksakan ng tass at dapat higit sa 0 ang iyong timbang at taas.")
