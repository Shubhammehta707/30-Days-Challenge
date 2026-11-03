""" Number Logic
Write a program to find all numbers between 1 and 10000 that are eqaul to the sum of the factorials of thier digits.
Example:145=1!+4!+5!"""

print("Numbers between 1 and 10000 equal to the sum of their digits' factorials:")

# Iterate through all numbers from 1 to 10000
for num in range(1, 10001):
    temp = num
    factorial_sum = 0
    
    # Process each digit of the number mathematically
    while temp > 0:
        digit = temp % 10
        
        # Calculate the factorial of the current digit
        digit_factorial = 1
        for i in range(1, digit + 1):
            digit_factorial *= i
            
        # Add the factorial to our running total
        factorial_sum += digit_factorial
        
        # Remove the last digit from temp
        temp //= 10
        
    # Check if the calculated sum matches the original number
    if factorial_sum == num:
        print(num)
