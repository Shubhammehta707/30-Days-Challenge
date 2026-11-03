""" 
    * * * * *
    *     *
    *   *
    * *
    * 
    
"""

# Set the size of the triangle (number of stars at the top)
size = 5

# Outer loop for each row from 1 to size
for i in range(1, size + 1):
    # Inner loop for each column position in the row
    # The row length decreases as i increases: size - i + 1
    for j in range(1, size - i + 2):
        
        # Condition to print a star:
        # 1. i == 1: The very first row (top horizontal edge)
        # 2. j == 1: The very first column (left vertical edge)
        # 3. j == size - i + 1: The last character of the current row (diagonal edge)
        if i == 1 or j == 1 or j == size - i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    # Move to the next line after completing the row
    print()
