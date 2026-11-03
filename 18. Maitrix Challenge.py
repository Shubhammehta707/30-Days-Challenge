""" Maitrix Challenge
Given a square matrix, find every element that is the smallest in its row and the largest in its column.Print the element 
and its position. If no such element exists,print an appropriate message."""

# A complete, properly filled 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 6, 7]
]

n = len(matrix)
found_any = False

for i in range(n):
    row_min = matrix[i][0]
    col_idx = 0
    for j in range(1, n):
        if matrix[i][j] < row_min:
            row_min = matrix[i][j]
            col_idx = j
            
    is_col_max = True
    for k in range(n):
        if matrix[k][col_idx] > row_min:
            is_col_max = False
            break
            
    if is_col_max:
        print(f"Element {row_min} found at Position (Row {i + 1}, Column {col_idx + 1})")
        found_any = True

if not found_any:
    print("No such element exists in the given matrix.")
