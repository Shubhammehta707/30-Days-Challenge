""" Second-Largest Distinct Number
Given a list of integers, find the second-largest distinct value using loops.
Example:[10, 25, 25, 8, 20] -> 20
Constraints:
• Do not use sort(), sorted(), or max(),
• Handle duplicate values,
• Display a suitable message if no second-largest distinct value exists."""

def find_second_largest_message(numbers):
    # Initialize both tracking variables to None
    largest = None
    second_largest = None

    for num in numbers:
        # 1. Initialize the largest value if it hasn't been set yet
        if largest is None:
            largest = num
        # 2. If the current number is bigger than the largest found so far
        elif num > largest:
            second_largest = largest
            largest = num
        # 3. If it's smaller than 'largest' but bigger than 'second_largest' (or second_largest is unset)
        elif num < largest:
            if second_largest is None or num > second_largest:
                second_largest = num
        # Note: If num == largest, we implicitly skip it to handle duplicates properly

    # Display the result or a suitable message based on the constraints
    if second_largest is not None:
        print(f"The second-largest distinct value is: {second_largest}")
    else:
        print("No second-largest distinct value exists in the provided list.")

# Test Example
example_list = [10, 25, 25, 8, 20]
find_second_largest_message(example_list)

#OR

# Input list
numbers =

# Initialize tracking variables
largest = None
second_largest = None

# Loop through each number manually
for num in numbers:
    if largest is None:
        largest = num
    elif num > largest:
        second_largest = largest
        largest = num
    elif num < largest:
        if second_largest is None or num > second_largest:
            second_largest = num

# Display the suitable message based on the result
if second_largest is not None:
    print(f"The second-largest distinct value is: {second_largest}")
else:
    print("No second-largest distinct value exists.")
