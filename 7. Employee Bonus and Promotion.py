""" Employee Bonus and Promotion
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
