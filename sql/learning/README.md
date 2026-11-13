# SQL learning

Worked SQL examples on a small demo database called `nova_retail` (a retail and e-commerce shop with 9 tables). The folders are numbered in study order: set up the database, learn the topics, then apply them to analytics, cleaning, warehousing, ETL and performance.

The files use MySQL syntax. The seed data has only a handful of rows per table, so results are small and easy to check by hand.

## Set up the database

Run the files in `00_database/` in this order:

1. `schema/` in number order: create the database, tables, constraints, indexes, views
2. `seed_data/` in number order: categories, customers, products, orders, order items, payments, inventory

Every other file starts with `USE nova_retail;`, so after that you can run any file on its own.

## Study path

| Folder | Content |
| --- | --- |
| `00_database/` | Schema and seed data for the 9 tables: customers, categories, products, orders, order_items, payments, inventory, employees, returns |
| `01_topics/` | 21 topics, 79 files (see below) |
| `02_analytics/` | Customer, finance, marketing, operations and sales analysis queries |
| `03_data_cleaning/` | General cleaning queries, duplicate handling, NULL handling |
| `04_advanced/` | Advanced window functions, cohort analysis, dynamic SQL, pivot and unpivot, rolling metrics |
| `05_data_warehouse/` | Fact and dimension tables, slowly changing dimensions, star schema, snowflake schema |
| `06_etl_pipelines/` | Audit logging, bronze-silver-gold pipeline, incremental loading, merge and upsert |
| `07_performance/` | Execution plans, indexing strategies, query optimization |

### Topics in `01_topics/`

| Group | Topics |
| --- | --- |
| Querying | 01 select, 02 filtering, 03 sorting and limiting, 04 aggregate functions, 05 grouping, 06 CASE statements, 07 string functions, 08 date functions |
| Combining data | 09 joins, 10 subqueries, 11 common table expressions, 12 window functions, 13 set operations |
| Database objects | 14 views and temp tables, 15 constraints and keys, 16 indexes, 17 stored procedures, 18 user-defined functions, 19 triggers, 20 transactions |
| Habits | 21 SQL best practices |

Practice questions live next door in [`../problem-solving/`](../problem-solving/README.md).
