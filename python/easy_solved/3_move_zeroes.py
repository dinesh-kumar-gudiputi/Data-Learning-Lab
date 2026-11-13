"""3. Move Zeroes
Difficulty: Easy
Source problem: LeetCode 283
Source: https://leetcode.com/problems/move-zeroes/description/

Task: Mutate the input list so zero values follow all nonzero values; preserve nonzero order and do not allocate a second array.
Example: `[4, 0, 2, 0]` becomes `[4, 2, 0, 0]`. Return `None`.
Check: All zeros; no zeros; a single value. Source inputs contain at least one value.
Practice: Stable in-place list manipulation. **Time:** 15 minutes.

Implement the function below and check its result with these examples.
"""

def move_zeroes(nums: list[int]) -> None:
    """
    Move all zeroes in the list to the end while maintaining the order of non-zero elements.
    
    Args:
    nums (list[int]): The input list of integers.
    
    Returns:
    None: The function modifies the list in place and returns None.
    """
    # Initialize a pointer for the position of the next non-zero element
    last_non_zero_found_at = 0
    
    # Iterate through the list
    for current in range(len(nums)):
        # If the current element is not zero, we need to move it to the last non-zero position
        if nums[current] != 0:
            # Swap the elements at last_non_zero_found_at and current
            nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
            # Move the pointer to the next position
            last_non_zero_found_at += 1
    return nums
print(move_zeroes([4, 0, 2, 0]))  # Output: [4, 2, 0, 0]
print(move_zeroes([0, 0, 0, 0]))  # Output: [0, 0, 0, 0]