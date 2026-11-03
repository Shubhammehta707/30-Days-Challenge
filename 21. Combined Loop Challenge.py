""" Combined Loop Challenge
Write a program that examines every pair o integers i and j from 1 to 20, subject to these rules:
1. Skip pair where i==j
2. skip pairs where both numbers are even.
3. stop the inner loop when i * j > 100.
4. print only pairs whose sum is a prime number.
5. count and display the total number of pairs printed.
Use nested loops and conditional statements to solve the problem."""

print("Pairs (i, j) matching all rules:")

pair_count = 0

# Outer loop for i from 1 to 20
for i in range(1, 21):
    # Inner loop for j from 1 to 20
    for j in range(1, 21):
        
        # Rule 1: Skip pairs where i == j
        if i == j:
            continue
            
        # Rule 2: Skip pairs where both numbers are even
        if i % 2 == 0 and j % 2 == 0:
            continue
            
        # Rule 3: Stop the inner loop when i * j > 100
        if i * j > 100:
            break
            
        # Rule 4: Print only pairs whose sum is a prime number
        pair_sum = i + j
        
        # Prime number verification logic
        is_prime = True
        if pair_sum < 2:
            is_prime = False
        else:
            for k in range(2, int(pair_sum ** 0.5) + 1):
                if pair_sum % k == 0:
                    is_prime = False
                    break
        
        # If the sum is prime, print the pair and update the counter
        if is_prime:
            print(f"({i}, {j}) -> Sum: {pair_sum}")
            pair_count += 1

# Rule 5: Count and display the total number of pairs printed
print(f"\nTotal number of matching pairs printed: {pair_count}")
