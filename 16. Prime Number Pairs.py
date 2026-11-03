""" Prime Number Pairs
Find all pairs of prime numbers between 1 and 200 whose difference is exactly 6.Print each pair only once."""

print("Prime number pairs between 1 and 200 with a difference of exactly 6:")

# Iterate through possible first numbers in the pair
for num1 in range(2, 201):
    
    # Check if num1 is prime
    is_prime1 = True
    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            is_prime1 = False
            break
            
    # If num1 is prime, check its partner (num1 + 6)
    if is_prime1:
        num2 = num1 + 6
        
        # Ensure the partner stays within the 1 to 200 boundary
        if num2 <= 200:
            
            # Check if num2 is prime
            is_prime2 = True
            for j in range(2, int(num2 ** 0.5) + 1):
                if num2 % j == 0:
                    is_prime2 = False
                    break
            
            # If both are prime, print the pair
            if is_prime2:
                print(f"({num1}, {num2})")
