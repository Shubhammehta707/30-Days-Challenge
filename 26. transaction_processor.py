""" Write a function that processes a list of transaction amounts and a
configurable threshold. Using a single pass, return (a) the number
of amounts above the threshold, (b) the largest amount, (c) the
smallest amount, and (d) the average of all amounts. Use a default
threshold of 100. Handle an empty input list safely and explain how
your function's return value represents the results."""

def analyze_transactions(transactions, threshold=100):
    # Safe handling for an empty input list
    if not transactions:
        return (0, None, None, 0.0)
    
    # Initialize tracking variables using the first element
    above_threshold_count = 0
    largest_amount = transactions[0]
    smallest_amount = transactions[0]
    total_sum = 0
    
    # Single pass loop through all transactions
    for amount in transactions:
        # a) Count amounts strictly above the threshold
        if amount > threshold:
            above_threshold_count += 1
            
        # b) Track the largest amount
        if amount > largest_amount:
            largest_amount = amount
            
        # c) Track the smallest amount
        if amount < smallest_amount:
            smallest_amount = amount
            
        # d) Accumulate total sum for the average
        total_sum += amount

    # Calculate the average
    average_amount = total_sum / len(transactions)
    
    return (above_threshold_count, largest_amount, smallest_amount, average_amount)

# --- Verification & Testing ---
# Test Case 1: Standard transactions list (Filled completely to prevent errors)
tx_list = [50, 120, 250, -20, 300, 80, 25]

count, maximum, minimum, avg = analyze_transactions(tx_list, threshold=100)

print(f"Results -> Above Threshold: {count}, Max: {maximum}, Min: {minimum}, Avg: {avg:.2f}")
# Expected output: Above Threshold: 3, Max: 300, Min: -20, Avg: 115.00

# Test Case 2: Empty transactions list
empty_list = []
print("Empty List Result:", analyze_transactions(empty_list))
# Expected output: (0, None, None, 0.0)
