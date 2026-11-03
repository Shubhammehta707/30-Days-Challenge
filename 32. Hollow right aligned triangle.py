"""
        *
      * *
    *   *
  *     *
* * * * *

"""

# Set the size of the triangle
size = 5

# Outer loop for each row from 1 to size
for i in range(1, size + 1):
    
    # 1. Inner loop to print leading spaces for right-alignment
    # Each star takes 2 characters worth of space ("* "), so we print pairs of spaces ("  ")
    for j in range(size - i):
        print("  ", end="")
        
    # 2. Inner loop to print the stars and hollow spaces within the row
    for k in range(1, i + 1):
        # Condition to print a star:
        # k == 1: The slanted diagonal edge
        # k == i: The rightmost vertical edge
        # i == size: The bottom horizontal edge
        if k == 1 or k == i or i == size:
            print("* ", end="")
        else:
            print("  ", end="")
            
    # Move to the next line after completing the row
    print()
