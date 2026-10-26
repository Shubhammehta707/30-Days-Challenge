"""Question 1:Pattern Programming
Print the following pattern for n=5:
1
212
32123
4321234
543212345"""

n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    
    for j in range(2,i+1):
        print(j,end="")
    print()
    
    
"""Question 2:Number Logic
Write a program to find all numbers between 1 and 10000 that are eqaul to the sum of the factorials of thier digits.
Example:145=1!+4!+5!"""

