"""2. Valid Anagram
Difficulty: Easy
Source problem: LeetCode 242
Source: https://leetcode.com/problems/valid-anagram/description/

Task: Decide whether two lowercase strings contain identical letter counts, regardless of order.
Example: `s="save", t="vase"` → `True`; `s="aab", t="abb"` → `False`.
Check: Unequal lengths; repeated letters; a single letter. Source inputs are nonempty lowercase English strings.
Practice: Strings and frequency comparison. **Time:** 15 minutes.

Implement the function below and check its result with these examples.
"""

def is_anagram(s: str, t: str) -> bool:
    #return sorted(s) == sorted(t)
    for char in set(s):
        if s.count(char) != t.count(char):
            return False
    return True
print("Test cases for is_anagram function:")
print(is_anagram("save", "vase"))  # Expected: True
print(is_anagram("aab", "abb"))    # Expected: False    
print(is_anagram("listen", "silent"))  # Expected: True