""" Pascal's Traingle
Accept the number of rows N and print Pascal's Triangle using for loops.
For N=5, the output should be:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1 
"""

n = 5  # Change this to int(input("Number of rows: "))
previous = []
for row_index in range(n):
    current = []
    for col in range(row_index + 1):
        if col == 0 or col == row_index:
            current.append(1)              # The edges of every row are 1.
        else:
            current.append(previous[col - 1] + previous[col])
    for _ in range(n - row_index - 1):
        print(" ", end="")
    for value in current:
        print(value, end=" ")
    print()
    previous = current                     # This row becomes the next row's parent.
