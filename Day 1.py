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


"""Q2. Very Advanced: Employee Bonus and Promotion Eligibility
Write a Python program that accepts an employee's annual salary, years of experience, performance rating (out of 10), and attendance percentage.
Requirements:
Print "Bonus Eligible" if experience is at least 3 years, rating is at least 8, and attendance is at least 90%.
Print "Promotion Eligible" if experience is at least 5 years and rating is at least 9.
Print "High Performer" if the rating is at least 9, regardless of the other conditions.
Each result must be checked independently.
If the salary is greater than 1,000,000, print "High Salary Band"
Restriction: Use independent if statements with appropriate logical operators. Multiple messages may appear."""

annual_salary = float(input("Enter your annual salary:"))
experience = float(input("Enter your years of experience:"))
rating = float(input("Enter your performance rating (out of 10):"))
attendence_percentage = float(input("Enter your attendence percentage:"))
if experience >= 3 and rating >= 8 and attendence_percentage >= 90:
    print("Bonus Eligible")
if experience >= 5 and rating >= 9:
    print("Promotion Eligible")
if rating >= 9:
    print("High Performer")
if annual_salary > 1000000:
    print("High Salary Band")
if experience < 3 and rating < 8 and attendence_percentage < 90:
    print("Not Eligible for Bonus")
if experience < 5 and rating < 9:
    print("Not Eligible for Promotion")
if rating < 9:
    print("Not High Performer") 
if annual_salary < 1000000:
    print("Not High Salary Band")


"""Q3. Expert Level: Nested if Admission and Scholarship System
Write a Python program for a college admission system using nested if statements only.
Accept these inputs:
Student age
Entrance exam score (out of 100)
Class 12 percentage
Family annual income
Requirements:
1.Check whether the student is at least 18 years old.
2.If eligible by age, check whether the entrance score is at least 75.
3.If the entrance score quallfies, check whether the Class 12 percentage is at least 60.
4.If all admission requirements are satisfied, print "Admission Approved".
5.Inside the approved admission block, check whether the family income is at most
₹300,000 and the entrance score is at least 90. 
6.If both scholarship conditions are satisfied, print "Full Scholarship Eligible". 
7. Otherwise, if admission requirements fail, print the specific reason for rejection.
Challenge: Design the nested conditions so the scholarship check runs only after admission is approved. Avoid elif, else, and compound shortcuts that replace the required nested structure."""

student_age = int(input("Enter your age:"))
score = float(input("Enter your Enterence Exam Score (out of 100):"))
percentage = float(input("Enter your Class 12 perctage:"))
family_income = int(input("Enter your Family annual income"))
if student_age >= 18:
    if score >= 75:
        if percentage >= 60:
            print("Admission Approved")
            if family_income<=300000 and score>=90:
                print("Full Scholarship Eligible.")
        if percentage < 60:
            print("Rejected,Class 12 percentage is less than 60")
    if score < 75:
        print("Rejected,Enterence Exam Score is less than 75")
if student_age < 18:
    print("Rejected,Underage")