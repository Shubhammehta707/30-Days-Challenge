""" Armstrong Numbers
Accept a positive integer N and print all Armstrong numbers from 1 to N using for loops.
An Armstrong number equals the sum of its digits, each raised to the power of the number of digits.
Example: 153 = 13 + 53 + 33
Constraint: Do not use string conversion to extract digits and do not use external libraries."""

N = 500000  # Replace with your desired positive integer N

# Pre-defined limits for digit counts (supports up to 7-digit numbers, expandable)
# Index matches the number of digits (e.g., 2-digit numbers are between 10 and 99)
limits = [0, 10, 100, 1000, 10000, 100000, 1000000, 10000000]

current_digits = 1

for num in range(1, N + 1):
    # Dynamically update the digit count as the loop progresses past boundaries
    if num >= limits[current_digits]:
        current_digits += 1
        
    # Extract digits and compute the power sum in line
    temp = num
    digit_sum = 0
    while temp > 0:
        digit_sum += (temp % 10) ** current_digits
        temp //= 10
        
    # Print if it matches the Armstrong condition
    if digit_sum == num:
        print(num)
