# SQL reference (MySQL)

Worked SQL examples on a small demo database called `nova_retail` (a retail and e-commerce shop with 9 tables). It is the study material behind the daily questions: one topic per file, with short examples you can run and change.

The files use MySQL syntax. The seed data has only a handful of rows per table, so results are small and easy to check by hand.

## Set up the database

Run the files in this order:

1. `database/schema/` in number order: create the database, tables, constraints, indexes, views
2. `database/seed_data/` in number order: categories, customers, products, orders, order items, payments, inventory

Every other file starts with `USE nova_retail;`, so after that you can run any file on its own.

## What is in here

| Folder | Content |
| --- | --- |
| `database/` | Schema and seed data for the 9 tables: customers, categories, products, orders, order_items, payments, inventory, employees, returns |
| `topics/` | 21 topics, 79 files (see below) |
| `analytics/` | Customer, finance, marketing, operations and sales analysis queries |
| `data_cleaning/` | General cleaning queries, duplicate handling, NULL handling |
| `advanced/` | Advanced window functions, cohort analysis, dynamic SQL, pivot and unpivot, rolling metrics |
| `data_warehouse/` | Fact and dimension tables, slowly changing dimensions, star schema, snowflake schema |
| `etl_pipelines/` | Audit logging, bronze-silver-gold pipeline, incremental loading, merge and upsert |
| `performance/` | Execution plans, indexing strategies, query optimization |
| `leetcode/` | 12 solved LeetCode problems: 4 easy, 4 medium, 4 hard |

### Topics

| Group | Topics |
| --- | --- |
| Querying | 01 select, 02 filtering, 03 sorting and limiting, 04 aggregate functions, 05 grouping, 06 CASE statements, 07 string functions, 08 date functions |
| Combining data | 09 joins, 10 subqueries, 11 common table expressions, 12 window functions, 13 set operations |
| Database objects | 14 views and temp tables, 15 constraints and keys, 16 indexes, 17 stored procedures, 18 user-defined functions, 19 triggers, 20 transactions |
| Habits | 21 SQL best practices |

The `leetcode/` solutions are separate from the daily questions in `easy/`, `medium/` and `hard/` one level up and do not use their numbering.
