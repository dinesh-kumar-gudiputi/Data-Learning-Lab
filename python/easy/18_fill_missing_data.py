"""
Question 18: Fill Missing Data
Source: LeetCode 2887 | Difficulty: Easy
https://leetcode.com/problems/fill-missing-data/
Assigned 2026-10-26 | Estimate: 10 minutes | Skill: Column-specific missing-value handling
Task: Replace missing quantity values with 0. Preserve existing quantities, every other column, row order and index.
Example: Columns name, quantity, price; rows ('Pen',None,2),('Book',4,8),('Bag',0,None). Expected ('Pen',0,2),('Book',4,8),('Bag',0,None).
Constraints and edge cases: Quantity is numeric or missing (None/NaN/pd.NA). A missing price must stay missing. Check empty input with the same columns, all quantities missing, and no missing quantities.
DA relevance: Apply a documented inventory cleaning rule without changing unrelated fields.
Requires pandas; source platform is an alternative if unavailable locally.
Status: Assigned, not completed.
"""
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
