"""
   *
   ***
   *****
   *******
   *********
   
"""

# Set the number of rows
rows = 5

# Loop through each row
for i in range(1, rows + 1):
    
    # Inner loop to print the increasing odd number of asterisks (1, 3, 5, 7, 9)
    for k in range(2 * i - 1):
        print("*", end="")
        
    # Move to the next line after completing the row
    print()
