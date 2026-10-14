Question 1 Scholarship Eligibility Trap
A college awards scholarships based on marks and family income.
Rules:
If any subject mark is below 35, the student fails.
Otherwise, calculate the average of 3 subjects.
Average ≥ 90 and income below ₹3,00,000: 100% scholarship.
Average ≥ 80 and income below ₹5,00,000: 50% scholarship.
Average ≥ 70: admission without scholarship.
Otherwise: admission rejected.
Tricky condition: A student scores 95, 96, and 30, with family income of ₹1,00,000. The average i high, but should the student receive a scholarship?
Task: Write the complete program with input validation and nested conditions.

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
          