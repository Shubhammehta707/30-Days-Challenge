""" Write a function that accepts a list of integers and returns the
length and starting index of the longest contiguous strictly
increasing segment. If multiple segments have the same maximum
length, return the earliest one. Do not create a second list of
segments and do not use sorting."""

def longest_increasing_segment(numbers):
    # Edge case: If the list is empty, there is no segment
    if not numbers:
        return (0, -1)
    
    n = len(numbers)
    
    # Variables to track the overall best segment found so far
    max_length = 1
    best_start_idx = 0
    
    # Variables to track the current segment we are measuring
    current_length = 1
    current_start_idx = 0
    
    # Loop through the list starting from the second element
    for i in range(1, n):
        # Check if the sequence is strictly increasing
        if numbers[i] > numbers[i - 1]:
            current_length += 1
        else:
            # The segment broke, evaluate if the completed segment is the longest
            # Using '>' (strict comparison) ensures we keep the earliest one in case of a tie
            if current_length > max_length:
                max_length = current_length
                best_start_idx = current_start_idx
                
            # Reset trackers to start a new segment at the current index
            current_length = 1
            current_start_idx = i

    # Final check to handle a segment that extends all the way to the end of the list
    if current_length > max_length:
        max_length = current_length
        best_start_idx = current_start_idx
        
    return max_length, best_start_idx

# --- Verification & Testing ---
# Test Case 1: Multiple segments of the same length
# Segments: [1, 3, 5] (len 3, start 0), [2, 4, 6] (len 3, start 4)
nums1 = [1, 3, 5, 2, 2, 4, 6, 1]
length, start_idx = longest_increasing_segment(nums1)
print(f"Test 1 -> Length: {length}, Starting Index: {start_idx}") 
# Expected output: Length: 3, Starting Index: 0 (earliest one)

# Test Case 2: Standard single longest segment
nums2 = [10, 22, 9, 33, 49, 50, 21, 60]
length, start_idx = longest_increasing_segment(nums2)
print(f"Test 2 -> Length: {length}, Starting Index: {start_idx}")
# Expected output: Length: 4, Starting Index: 2 ([9, 33, 49, 50])
