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
