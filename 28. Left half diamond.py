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
print("Left-aligned diamond-half pattern:")

# Part 1: Top half of the pattern (increasing from 1 to 5)
for i in range(1, peak + 1):
    for j in range(i):
        print("*", end="")
    print()

# Part 2: Bottom half of the pattern (decreasing from 4 down to 1)
for i in range(peak - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
