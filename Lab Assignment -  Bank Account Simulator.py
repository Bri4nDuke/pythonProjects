#Lab Assignment -  Bank Account Simulator
#By: Brian Duke
#Date: 4/03/2025
#This program will ask you for account information and then simulate a bank account.

accountNumber = "1234567890"
accountHolder = "Duke, Brian"
balance = 0.00

#Display account information
print("Hello, Welcome to Duke Bank!")
print("\n--- Account Information ---")
print("Account Number:  ", accountNumber)
print("Account Holder:  ", accountHolder)
print("Account Balance: ", balance)
print("---------------------------\n")

#Prompt the user for actions
deposit = input("Enter Deposit: ")
balance = float(balance) + float(deposit)
print("Account Balance: ", balance)

withdraw = input("Enter Withdraw: ")
if float(withdraw) > float(balance):
    print("Insufficient funds!")
elif float(withdraw) < 0:
    print("Invalid withdraw amount!")
else:
    balance = float(balance) - float(withdraw)
    print("Withdraw successful!")
    print("Account Balance: ", balance)
    
print("\nThank you for choosing Brian Bank!")
    