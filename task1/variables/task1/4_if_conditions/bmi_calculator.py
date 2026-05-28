height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height * height)

print("BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")

elif bmi >= 25 and bmi < 30:
    print("Overweight")

else:
    print("Obesity")