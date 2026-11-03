""" Perfect Numbers in a Range
Accept a number N and print all perfect numbers from 1 to N.
A perfect number equals the sum of its positive proper divisors.
Example: 28 1 + 2 + 4+ 7 + 14
Constraints:
• Use nested for loops.
• Do not use external libraries,
• Do not include the number itself when summing its divisors."""

# Accept the number N from the user
num = int(input("Enter a number: "))
print("Perfect numbers between 1 and", num, "are:")

# Outer loop to iterate through each number from 1 to N
for i in range(1, num + 1):
    sum_of_divisors = 0
    
    # Inner loop to find proper divisors (excluding the number itself)
    for j in range(1, i):
        if i % j == 0:
            sum_of_divisors += j
            
    # Check if the sum of divisors equals the original number
    if sum_of_divisors == i:
        print(i)
