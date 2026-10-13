"""Q1. Basic + Challenging: Smart Transaction Validator
Write a Python program that accepts a bank balance and a withdrawal amount.
Requirements:
Check whether the withdrawal amount is positive.
Check whether the amount is a multiple of 100.
Check whether the account has sufficient balance.
Print "Transaction Successful" only if all three conditions are satisfied.
Otherwise, print the appropriate reason for rejection.
Restriction: Use only if statements and logical operators. Do not use elif or else."""

# balance = 5000
# withdrawal_amount=int(input("Enter the amount to withdraw: "))
# if withdrawal_amount <= 0 :
#     print("Withdrawal amount cannot be negative or Zero")
# if withdrawal_amount % 100 != 0:
#     print("Withdrawal amount is not multiple of 100")
# if withdrawal_amount > 5000:
#     print("Insufficient balance")
# if 0<withdrawal_amount<5000 and withdrawal_amount % 100 == 0:
#     print ("Transaction Successfull")


"""Q2. Very Advanced: Employee Bonus and Promotion Eligibility

Write a Python program that accepts an employee's annual salary, years of experience, performance rating (out of 10), and attendance percentage.

Requirements:

Print "Bonus Eligible" if experience is at least 3 years, rating is at least 8, and attendance is at least 90%.

Print "Promotion Eligible" if experience is at least 5 years and rating is at least 9.

Print "High Performer" if the rating is at least 9, regardless of the other conditions.

Each result must be checked independently.

If the salary is greater than 1,000,000, print "High Salary Band"

Restriction: Use independent if statements with appropriate logical operators. Multiple messages may appear."""

annual_salary = float(input("Enter your annual salary"))
experience = float(input("Enter your years of experience"))
rating = float(input("Enter your performance rating (out of 10)"))
attendence_percentage = float(input("Enter your attendence percentage"))
if experience >= 3 and rating >= 8 and attendence_percentage >= 90:
    print("Bonus Eligible")
if experience >= 5 and rating >= 9:
    print("Promotion Eligible")
if rating >= 9:
    print("High Performer")
if annual_salary > 1000000:
    print("High Salary Band")
