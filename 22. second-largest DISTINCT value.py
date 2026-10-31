""" Given a list of integers, find the second-largest DISTINCT value
without sorting the list and without using max(), min(), or set().
If fewer than two distinct values exist, return None."""

nums = [22,29,5,20,25,26]
first = 0
second = 0
for num in nums:
    if num == first:
        continue
    
    if first is None or num > first:
        second = first
        first = num
        
    elif second is None or num > second :
        second = num

print("First largest number is" ,first)
print("Second largest number is",second)
