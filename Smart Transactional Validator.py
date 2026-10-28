"""Q1. Basic + Challenging: Smart Transaction Validator
Write a Python program that accepts a bank balance and a withdrawal amount.
Requirements:
Check whether the withdrawal amount is positive.
Check whether the amount is a multiple of 100.
Check whether the account has sufficient balance.
Print "Transaction Successful" only if all three conditions are satisfied.
Otherwise, print the appropriate reason for rejection.
Restriction: Use only if statements and logical operators. Do not use elif or else."""

balance = 5000
withdrawal_amount=int(input("Enter the amount to withdraw: "))
if withdrawal_amount <= 0 :
    print("Withdrawal amount cannot be negative or Zero")
if withdrawal_amount % 100 != 0:
    print("Withdrawal amount is not multiple of 100")
if withdrawal_amount > 5000:
    print("Insufficient balance")
if 0<withdrawal_amount<5000 and withdrawal_amount % 100 == 0:
    print ("Transaction Successfull")
