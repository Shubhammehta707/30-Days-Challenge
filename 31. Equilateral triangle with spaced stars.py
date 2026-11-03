""" 
    *
   * *
  * * *
 * * * *
* * * * * 

"""

# Set the number of rows for the pyramid
rows = 5

# Loop through each row from 1 to 5
for i in range(1, rows + 1):
    
    # 1. Print leading spaces to center-align the row
    for j in range(rows - i):
        print(" ", end="")
        
    # 2. Print the asterisks followed by a space
    for k in range(i):
        print("* ", end="")
        
    # Move to the next line after completing the row
    print()
