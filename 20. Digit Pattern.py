""" Digit Pattern
Print all numbers from 100 to 999 whose digits are strictly increasing from left to right and whose digit sum is divisible by 3.
Example: 123 qualifies because its digits increse and 1+2+3=6."""

print("Numbers from 100 to 999 with strictly increasing digits and a digit sum divisible by 3:")

count = 0

# Loop through all 3-digit numbers
for num in range(100, 1000):
    # Extract digits mathematically
    # Example for 123:
    hundreds = num // 100         # 123 // 100 = 1
    tens = (num // 10) % 10       # 12 // 10 = 1, remainder 2
    ones = num % 10               # Remainder 3
    
    # Constraint 1: Digits must be strictly increasing from left to right
    if hundreds < tens and tens < ones:
        
        # Calculate the sum of the digits
        digit_sum = hundreds + tens + ones
        
        # Constraint 2: The sum of digits must be divisible by 3
        if digit_sum % 3 == 0:
            print(num)
            count += 1

print(f"\nTotal numbers found: {count}")
