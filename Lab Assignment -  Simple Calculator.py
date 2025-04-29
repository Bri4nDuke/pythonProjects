# Lab Assignment - Simple Calculator
# By: Brian Duke
# Date: 3/27/2025
# This program will ask you for two numbers and then I will add, subtract, multiply, and divide them.

print("Hello, I am a simple calculator.")
print("I will ask you for two numbers and then I will add, subtract, multiply, and divide them.")

firstNumber = float(input("First Number: "))
secondNumber = float(input("Second Number: "))

sum_result = firstNumber + secondNumber
difference = firstNumber - secondNumber
product = firstNumber * secondNumber

# Check for division by zero
if secondNumber != 0:
    quotient = firstNumber / secondNumber
else:
    quotient = "Undefined (cannot divide by zero)"

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)