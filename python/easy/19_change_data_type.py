"""
Question 19: Change Data Type
Source: LeetCode 2886 | Difficulty: Easy
https://leetcode.com/problems/change-data-type/
Assigned 2026-10-26 | Estimate: 10 minutes | Skill: Data type validation
Task: Convert grade from a floating-point column to an integer column. Preserve other columns, rows and index.
Example: Columns student_id,name,age,grade; rows (1,'Ada',21,82.0),(2,'Ben',22,0.0). Expected grades 82 and 0 with integer dtype; other values unchanged.
Constraints and edge cases: Practice inputs have finite, nonmissing, whole-valued float grades in 0..100. No rounding policy is needed. Check one row, zero, 100, and verify dtype as well as values.
DA relevance: Give analysis columns explicit, consistent types.
Requires pandas; source platform is an alternative if unavailable locally.
Status: Assigned, not completed.
"""
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
