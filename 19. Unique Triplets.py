""" Unique Triplets
Given a list of integers and a target value, find all unique triplets whose sum equals the target.Do not use sets, dictionaries, 
or sorting. Avoid duplicate triplets in the output."""

# Sample inputs
numbers = [1, 2, -1, 0, 4, -2, 1]
target = 2

# This list will hold the unique triplets we find
unique_triplets = []

n = len(numbers)

# Three nested loops to find every possible combination of 3 distinct items
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            
            # Check if the sum of the triplet matches the target
            if numbers[i] + numbers[j] + numbers[k] == target:
                current_triplet = [numbers[i], numbers[j], numbers[k]]
                
                # Check manually if this triplet combination already exists in our results
                is_duplicate = False
                for triplet in unique_triplets:
                    
                    # We need to check all structural permutations because the list isn't sorted
                    # Count occurrences of each number to ensure an exact combination match
                    t_counts = [0, 0, 0]
                    c_counts = [0, 0, 0]
                    
                    # Track matching elements manually
                    match_count = 0
                    temp_current = list(current_triplet)
                    
                    for item in triplet:
                        if item in temp_current:
                            temp_current.remove(item)
                            match_count += 1
                            
                    if match_count == 3:
                        is_duplicate = True
                        break
                
                # If it's a completely new unique combination, save it
                if not is_duplicate:
                    unique_triplets.append(current_triplet)

# Print the final results
print(f"Unique triplets that sum to {target}:")
if unique_triplets:
    for triplet in unique_triplets:
        print(triplet)
else:
    print("No triplets found.")
