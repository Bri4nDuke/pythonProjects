#Lab Assignment -  Simple Interest Calculator
#By: Brian Duke
#Date: 4/03/2025
#This program will ask you for principal, rate, and time and then I will calculate the simple interest.

print("Hello, I am a simple interst calculator.")
print("I will ask you for principal, rate, and time and then I will calculate the simple interest.\n")

principal = float (input("Principal Amount ($): "))
percentage = float (input("Percentage (%): "))
time = float (input("Time (years): "))
simpleInterest = (principal * percentage * time) / 100
totalAmount = principal + simpleInterest

print("Simple Interest: ", simpleInterest)
print("Total Amount: ", totalAmount)