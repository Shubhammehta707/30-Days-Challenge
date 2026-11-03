""" Write a function that finds the first pair of different list positions
whose values add up to a target. Return the two indices, or None if
no pair exists. Do not sort the list. If several pairs are possible,
return the pair with the smallest second index, and for that index the
smallest first index."""

def find_target_pair(numbers, target):
    n = len(numbers)
    
    # Outer loop loops over the second index first to guarantee we evaluate 
    # smaller second indices before larger ones.
    for j in range(n):
        # Inner loop checks positions before 'j' from left to right
        for i in range(j):
            # Check if the values at these different positions add up to the target
            if numbers[i] + numbers[j] == target:
                return (i, j)
                
    # Return None if no matching pair is found
    return None

# --- Verification & Testing ---
# Test Case 1: Multiple pairs possible
# Pairs that sum to 6: 
# (pos 0 and pos 4) -> 2 + 4 = 6 (j = 4)
# (pos 1 and pos 3) -> 3 + 3 = 6 (j = 3) <- Smallest second index
nums1 = [2, 3, 7, 3, 4]
print("Test 1 Result:", find_target_pair(nums1, 6))  # Expected output: (1, 3)

# Test Case 2: No pair exists
nums2 = [1, 2, 3, 4]
print("Test 2 Result:", find_target_pair(nums2, 10)) # Expected output: None
