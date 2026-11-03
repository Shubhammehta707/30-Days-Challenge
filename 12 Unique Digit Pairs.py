""" Unique Digit Pairs
Accept a positive integer and find all pairs of digits whose sum equals a target entered by the user.
Example: Number 1224, target 6
Possible digit pairs include 2 + 4 = 6.
Constraints:
• Use loops and arithmetic operations.
• Do not convert the number into a string.
• Avoid printing the same digit-position pair twice.
• Handle repeated digits correctly."""

# Accept user inputs
num = int(input("Enter a positive integer: "))
target = int(input("Enter the target sum: "))

# Step 1: Extract digits mathematically into a list
digits = []
temp = num

while temp > 0:
    digit = temp % 10
    digits.append(digit)
    temp = temp // 10

# The digits are extracted from right to left, so reverse to match original order
digits.reverse()

print(f"Unique position pairs in {num} that sum to {target}:")

# Step 2: Use nested loops to find digit pairs by their positions
n = len(digits)
found_any = False

for i in range(n):
    for j in range(i + 1, n):
        if digits[i] + digits[j] == target:
            print(f"{digits[i]} (at pos {i+1}) + {digits[j]} (at pos {j+1}) = {target}")
            found_any = True

if not found_any:
    print("No pairs found.")
