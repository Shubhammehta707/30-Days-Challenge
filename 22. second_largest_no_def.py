""" Given a list of integers, find the second-largest DISTINCT value
without sorting the list and without using max(), min(), or set().
If fewer than two distinct values exist, return None."""

# Input list
numbers = [10, 25, 25, 8, 20]

# Initialize tracking variables to None
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

# The final variable 'second_largest' will naturally be 'None' 
# if fewer than two distinct values exist.
result = second_largest

# Display the final output
print("Result:", result)

#OR

def find_second_largest_none(numbers):
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None:
            largest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif num < largest:
            if second_largest is None or num > second_largest:
                second_largest = num

    # Return None directly if it doesn't exist, otherwise return the value
    return second_largest

# Test Example
example_list = [10, 25, 25, 8, 20]
result = find_second_largest_none(example_list)
print(f"Returned value: {result}")
