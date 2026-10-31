""" Employee Bonus and Promotion Eligibility
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
