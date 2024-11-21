# This Python code snippet is calculating the Body Mass Index (BMI) based on the user's input for
# height and weight. Here's a breakdown of what each part does:
height = int(input("What is your height\n"))

weight= int(input("What is your weight\n"))

bmi = (weight/(height**2))

if bmi < 18.5:print("Underweight")

elif 18.5 <= bmi < 24.9:print("Normal Weight")

elif 25<= bmi <29.9:print("Overweight")

else:print("Obese")