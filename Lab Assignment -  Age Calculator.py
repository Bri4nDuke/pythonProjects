#Lab Assignment -  Age Calculator
#By: Brian Duke
#Date: 3/27/2025
#This program will ask the user for their birth year and then calculate their age.

print("Hello, I am an age calculator.")
print("I will ask you how many years in the future they want to calculate their age for.")

age = int (input("Current Age: "))
years = int (input("Years to Calculate: "))
futureAge = age + years
print("In", years, "you will be", futureAge, "years old.")