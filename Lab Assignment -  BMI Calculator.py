#Lab Assignment -  Body Mass Index (BMI) Calculator
#By: Brian Duke
#Date: 4/03/2025
#This program will ask you for weight and height and then I will calculate the BMI.

print("Hello, I am a simple BMI calculator.")
print("I will ask you for weight and height and then I will calculate the BMI.\n")

weight = float (input("Weight (kg): "))
height = float (input("Height (meters): "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")