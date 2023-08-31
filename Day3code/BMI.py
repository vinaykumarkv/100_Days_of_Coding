# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=weight/(height**2)
bmi = round(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
if 18.5 < bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
if 25 < bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
if 30 < bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")