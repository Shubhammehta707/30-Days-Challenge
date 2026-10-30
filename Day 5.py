"""Advance Question 1:
Given a list of integers, find the second-largest DISTINCT value
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


"""Advance Question 2:
Write a function that receives a list of student records, where each
record contains a student's name and a list of marks. In one pass
through the records, determine the student with the highest average,
count how many students passed every subject, and calculate the
class-wide average of all individual marks. Handle empty records and
students with no marks without crashing."""

"""Advance Question 3:
Write a function that finds the first pair of different list positions
whose values add up to a target. Return the two indices, or None if
no pair exists. Do not sort the list. If several pairs are possible,
return the pair with the smallest second index, and for that index the
smallest first index."""

"""Advance Question 4:
Write a function that accepts a list of integers and returns the
length and starting index of the longest contiguous strictly
increasing segment. If multiple segments have the same maximum
length, return the earliest one. Do not create a second list of
segments and do not use sorting."""

"""Advance Question 5:
Write a function that processes a list of transaction amounts and a
configurable threshold. Using a single pass, return (a) the number
of amounts above the threshold, (b) the largest amount, (c) the
smallest amount, and (d) the average of all amounts. Use a default
threshold of 100. Handle an empty input list safely and explain how
your function's return value represents the results."""
