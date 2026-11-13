"""
Question 16: Drop Missing Data
Source: LeetCode 2883 | Difficulty: Easy
https://leetcode.com/problems/drop-missing-data/
Assigned 2026-10-21 | Skill: Missing-value cleaning | Estimate: 12 minutes
Task: Remove rows whose name is missing; retain other rows and columns in their original order. For this practice, preserve original index labels. An empty string is not a missing value.
Input and expected output: Columns: student_id, name, age. Rows: (10,'Ada',21),(11,None,22),(12,'',23),(13,'Ben',24). Expected retained rows: (10,'Ada',21),(12,'',23),(13,'Ben',24); indices 0,2,3.
Constraints/edges: Input is a pandas DataFrame. name may contain None/NaN/pd.NA. Consider all names present, all missing and empty input with the same columns. Do not drop valid names merely because another field is missing.
DA relevance: Prevent missing identifiers from contaminating analysis.
Requires pandas; use the source platform if pandas is unavailable locally.
Status: Assigned, not completed.
"""
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
