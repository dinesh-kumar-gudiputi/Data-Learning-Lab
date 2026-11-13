"""1. Contains Duplicate
Difficulty: Easy
Source problem: LeetCode 217
Source: https://leetcode.com/problems/contains-duplicate/description/

Task: Detect whether any integer occurs more than once.
Example: `[8, 3, 8]` → `True`; `[8, 3, 1]` → `False`.
Check: One value; all values repeated; negative values. Source inputs contain at least one value.
Practice: Lists and membership; recognizing duplicate records. **Time:** 15 minutes.

Implement the function below and check its result with these examples.
"""
from pyparsing import nums


def contains_duplicate(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print("Test cases for contains_duplicate function:")
print(contains_duplicate([8, 3, 8]))  # Expected: True
print(contains_duplicate([8, 3, 1]))  # Expected: False