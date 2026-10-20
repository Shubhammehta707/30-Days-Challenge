"""Question 1 Scholarship Eligibility Trap
A college awards scholarships based on marks and family income.
Rules:
If any subject mark is below 35, the student fails.
Otherwise, calculate the average of 3 subjects.
Average ≥ 90 and income below ₹3,00,000: 100% scholarship.
Average ≥ 80 and income below ₹5,00,000: 50% scholarship.
Average ≥ 70: admission without scholarship.
Otherwise: admission rejected.
Tricky condition: A student scores 95, 96, and 30, with family income of ₹1,00,000. The average i high, but should the student receive a scholarship?
Task: Write the complete program with input validation and nested conditions."""

# 1. Input Collection
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
income = float(input("Enter family income (₹): "))

# 2. Input Validation using if-elif-else
if m1 < 0 or m1 > 100:
    print("Invalid Input: Subject 1 marks must be between 0 and 100.")
elif m2 < 0 or m2 > 100:
    print("Invalid Input: Subject 2 marks must be between 0 and 100.")
elif m3 < 0 or m3 > 100:
    print("Invalid Input: Subject 3 marks must be between 0 and 100.")
elif income < 0:
    print("Invalid Input: Income cannot be negative.")

# 3. Main Rule Processing
else:
    # Rule 1: Check if any subject mark is below 35
    if m1 < 35:
        print("Result: Student fails. Admission rejected.")
    elif m2 < 35:
        print("Result: Student fails. Admission rejected.")
    elif m3 < 35:
        print("Result: Student fails. Admission rejected.")
    else:
        # Calculate average if all subjects passed
        average = (m1 + m2 + m3) / 3
        print(f"Average Marks: {average:.2f}")
        
        # Nested scholarship rules
        if average >= 90:
            if income < 300000:
                print("Result: Admission Granted with 100% Scholarship.")
            elif income < 500000:
                print("Result: Admission Granted with 50% Scholarship.")
            else:
                print("Result: Admission Granted without Scholarship.")
                
        elif average >= 80:
            if income < 500000:
                print("Result: Admission Granted with 50% Scholarship.")
            else:
                print("Result: Admission Granted without Scholarship.")
                
        elif average >= 70:
            print("Result: Admission Granted without Scholarship.")
            
        else:
            print("Result: Admission Rejected (Average below 70).")


"""Question 2 ATM Withdrawal Logic
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
rating=float(input("Enter your rating: "))
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
          