"""
Question 4: Two Sum
Source: LeetCode 1 | Difficulty: Easy
https://leetcode.com/problems/two-sum/
Skill: Sequence and data processing | Estimated time: 12 minutes
Task: Return the two distinct indices whose values total target. Exactly one pair exists; either index order is accepted.
Example: nums=[4,8,1], target=9 -> [1,2]
Constraints/edge cases: 2..10000 values; values and target within -10^9..10^9. Duplicates and negatives are possible.
DA/DE relevance: Matching records by a combined value.
Status: Assigned; starter only, not evidence of completion.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two distinct indices in the list such that their values sum up to the target.
    
    Args:
    nums (list[int]): The input list of integers.
    target (int): The target sum.
    
    Returns:
    list[int]: A list containing the two indices of the numbers that add up to the target.
    """
    # Create a dictionary to store the value and its corresponding index
    num_to_index = {}
    
    # Iterate through the list
    for index, num in enumerate(nums):
        # Calculate the complement that would sum with the current number to reach the target
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the current number and its complement
            return [num_to_index[complement], index]
        
        # Store the current number and its index in the dictionary
        num_to_index[num] = index
    
    # If no solution is found, return an empty list (though the problem guarantees one solution)
    return []


# Example usage:
print(two_sum([4, 8, 1], 9))  # Output: [1, 2]
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))  # Output: [1, 2]
print(two_sum([3, 3], 6))  # Output: [0, 1


