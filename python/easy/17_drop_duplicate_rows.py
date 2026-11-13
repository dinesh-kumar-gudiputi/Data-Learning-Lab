"""
Question 17: Drop Duplicate Rows
Source: LeetCode 2882 | Difficulty: Easy
https://leetcode.com/problems/drop-duplicate-rows/
Assigned 2026-10-21 | Skill: Key-based deduplication | Estimate: 12 minutes
Task: Remove repeated emails, retaining the first row for each email in input order. Preserve all columns and, for this practice, original index labels.
Input and expected output: Columns: customer_id, name, email. Rows: (7,'Ada','a@demo.test'),(8,'Ben','b@demo.test'),(9,'Cia','a@demo.test'). Expected first two rows; indices 0,1.
Constraints/edges: For this practice emails are non-NULL strings; compare exact values, without case normalization. First means input order, not smallest customer_id. Consider no duplicates, all emails equal and empty input with the same columns.
DA relevance: Keep one consistent customer record per business key.
Requires pandas; use the source platform if pandas is unavailable locally.
Status: Assigned, not completed.
"""
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
