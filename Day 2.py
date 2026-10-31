""" ATM Withdrawal Logic
Create an ATM program with a balance of ₹15,000.
Rules:
• Correct PIN: 4321.
• Withdrawal must be positive.
• The balance must never fall below ₹2,000.
• Withdrawals above ₹10,000 require manager approval.
• An incorrect PIN must prevent all further transactions.
Tricky condition: The balance is ₹12,000 and the customer tries to withdraw ₹11,000 without manager approval.
Task: Use nested if statements to handle every condition and display the correct remaining balance"""

balance = 15000
correct_pin = 4321
entered_pin = int(input("Enter your 4 digit pin: "))
withdrawal_amount=int(input("Enter amount to withdraw: "))
if entered_pin == correct_pin:
  print("Pin is correct")
  if withdrawal_amount>0:
    if balance - withdrawal_amount>=2000:
      if withdrawal_amount > 10000:
        manager_approval=(input("yes or no: "))
        if manager_approval=="yes":
          print("Amount withdrawal successfully")
        else:
          print("Manager permission required ")
  else:
    print("Amount can't be negative impact ")
else:
  print("Invalid Pin")
remaining_balance=balance-withdrawal_amount
print("Remaining amount", remaining_balance)


"""Question 3
Triangle Classification Puzzle
Accept three side lengths and classify the triangle.
Rules:
All sides must be positive.
The sum of any two sides must exceed the third side.
Classify it as equilateral, isosceles, or scalene.
Also check whether it is right-angled using the Pythagorean theorem.
Tricky condition: Inputs are 1, 2, 3. The sides look almost valid, but they do not form a triangle.
Task: Reject invalid triangles before checking their type or angle."""             
            
s1=int(input("enter side 1:-"))   
s2=int(input("enter side 2:-"))
s3=int(input("enter side 3:-"))
if s1>0 and s2>0 and s3>0:
    if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
        if s1**2+s2**2==s3**2 or s2**2+s3**2==s1**2 or s3**2+s1**2==s2**2:
            print("right angle triangle")
        if s1==s2==s3:
            print("equilateral")
        elif s1==s2 or s2==s3 or s1==s3:
            print("isosceles")
        else:
            print("scalene")
    else:
        print("side is not corret")        
else:
    print("negative side invaid")


"""Question 4
Employee Bonus and Promotion
Determine an employee's bonus and promotion eligibility.
Rules:
1.Experience ≥ 10 years and rating ≥ 4.5: 25% bonus and promotion.
2.Experience ≥ 10 years and rating ≥ 3.5: 15% bonus, no promotion.
3.Experience ≥ 5 years and rating ≥ 4.0: 12% bonus.
4.Experience below 5 years and rating ≥ 4.5: 8% bonus.
5.All other cases: no bonus.
Tricky condition: An employee has 12 years of experience but a rating of 3.2.
Task: Accept salary, experience, and rating; calculate the bonus amount and promotion status. Validate all inputs."""

salary=float(input("Enter your salary: "))
experience=int(input("Enter your experience in years: "))
rating=float(input("Enter your rating (out of 10): "))
if experience>=10 and rating>=4.5:
  bonus=salary*0.25
  salary=salary*0.25+salary
  print("bonus", bonus)
  print("salary",salary)
  print("25% bonus and promotion")
elif experience>=10 and rating>=3.5:
  bonus=salary*0.15
  salary=salary*0.15+salary 
  print("bonus",bonus)
  print("salary",salary)
  print("15% bonus and no promotion")
elif experience>=5 and rating>=4.0:
  bonus=salary*0.12
  salary=salary*0.12-salary
  print("bonus",bonus)
  print("salary",salary)
  print("12% bonus")
elif experience<5 and rating>=4.5:
  bonus=salary*0.8
  salary=salary*0.8+salary  
  print("bonus",bonus)
  print("salary",salary)
  print("8% bonus")
else:
  print("no bonus")


"""Question 5 
Login Security with Multiple Conditions
Build a login verification program.
Rules:
1. Username must be correct.
2. Password must be correct.
3. Account must be active.
4. OTP must be correct.
5. After three failed login attempts, lock the account.
Tricky condition: The username and password are correct, but the account is inactive and the OTP is also incorrect.
Task: Use nested conditions and logical operators to identify the exact failure reason. The program should stop authentication as soon as a required check fails."""

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"
IS_ACCOUNT_ACTIVE = False
CORRECT_OTP = "123456"

failed_attempts = 0

user_in = input("Entet your username: ")
pass_in = input("Enter your password: ")
otp_in = input("Enter your otp: ")

print("--- Starting Login Verification ---")

if failed_attempts >= 3:
    print("Authentication Failed: Account is locked due to too many failed attempts.")
else:
    if user_in == CORRECT_USERNAME:
        if pass_in == CORRECT_PASSWORD:
            if IS_ACCOUNT_ACTIVE:
                if otp_in == CORRECT_OTP:
                    print("Authentication Successful: Welcome!")
                    failed_attempts = 0
                else:
                    failed_attempts = failed_attempts + 1
                    print("Authentication Failed: OTP is incorrect.")
                    if failed_attempts >= 3:
                        print("Notice: Account has been locked.")
            else:
                print("Authentication Failed: Account is inactive.")
        else:
            failed_attempts = failed_attempts + 1
            print("Authentication Failed: Password is incorrect.")
            if failed_attempts >= 3:
                print("Notice: Account has been locked.")
    else:
        failed_attempts = failed_attempts + 1
        print("Authentication Failed: Username is incorrect.")
        if failed_attempts >= 3:
            print("Notice: Account has been locked.")
          
