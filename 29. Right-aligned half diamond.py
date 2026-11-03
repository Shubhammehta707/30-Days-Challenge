""" 
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    * 
    
"""

# Set the peak number of stars (the widest row)
peak = 5

print("Right-aligned diamond-half pattern:")

# Part 1: Top half of the pattern (increasing stars, decreasing spaces)
for i in range(1, peak + 1):
    # Print leading spaces
    for j in range(peak - i):
        print(" ", end="")
    # Print stars
    for k in range(i):
        print("*", end="")
    print()

# Part 2: Bottom half of the pattern (decreasing stars, increasing spaces)
for i in range(peak - 1, 0, -1):
    # Print leading spaces
    for j in range(peak - i):
        print(" ", end="")
    # Print stars
    for k in range(i):
        print("*", end="")
    print()

