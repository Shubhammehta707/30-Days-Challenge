""" Write a function that receives a list of student records, where each
record contains a student's name and a list of marks. In one pass
through the records, determine the student with the highest average,
count how many students passed every subject, and calculate the
class-wide average of all individual marks. Handle empty records and
students with no marks without crashing."""

records = [
    ("Asha", [78, 82, 91]),
    ("Ravi", [55, 39, 70]),
    ("Meera", [88, 92, 84]),
    ("NoMarks", [])
]

best_name = None
best_average = None
passed_all_count = 0
mark_total = 0
mark_count = 0

for name, marks in records:
    if not marks:
        continue
    student_total = 0
    passed_every_subject = True
    for mark in marks:
        student_total += mark
        mark_total += mark
        mark_count += 1
        if mark < 40:
            passed_every_subject = False
    average = student_total / len(marks)
    if best_average is None or average > best_average:
        best_average = average
        best_name = name
    if passed_every_subject:
        passed_all_count += 1

class_average = mark_total / mark_count if mark_count else None
print("Highest-average student:", best_name, "Average:", best_average)
print("Students passing every subject:", passed_all_count)
print("Class average:", class_average)
