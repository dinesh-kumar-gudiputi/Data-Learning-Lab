# SQL problem solving

Daily SQL questions for data analyst and data engineering roles. Every question is one `.sql` file: the task, the source link, the expected result, a runnable sample table and a place for your answer.

## Progress

| Level | Assigned | Solved |
| --- | ---: | ---: |
| [Easy](easy/README.md) | 24 | 5 |
| [Medium](medium/README.md) | 4 | 0 |
| [Hard](hard/README.md) | 0 | 0 |

## Folders

| Folder | What it holds |
| --- | --- |
| `easy/`, `medium/`, `hard/` | Assigned questions, stored once under their LeetCode difficulty, plus an index of the level |
| `solved/easy/`, `solved/medium/`, `solved/hard/` | Finished questions. Move a file here when it is solved and reviewed |
| [`earlier-solutions/`](earlier-solutions/README.md) | 12 LeetCode solutions from before the daily routine |

Question numbers are one sequence for the whole SQL track and keep counting across levels. The number in the file name is this repo's own counter; the source platform's problem ID is inside the file.

## Run a question

Each file creates its own sample tables. Write your query under `-- YOUR ANSWER`, then run it in a fresh SQLite session:

```sh
cd sql/problem-solving
sqlite3
.headers on
.mode column
.read easy/10_not_boring_movies.sql
.quit
```

On LeetCode, paste only your answer query, not the setup. The files target ANSI/PostgreSQL SQL and the setup also runs in SQLite. Dialects differ, for example `CHAR_LENGTH(content)` in PostgreSQL and `LENGTH(content)` in SQLite, so pick the dialect before you run.

## Routine

Monday to Friday at 19:00 (Europe/Berlin), 5 SQL questions. Difficulty rises with reviewed work, and earlier questions come back for recall. Commit with a clear message, for example `practice: solve question 10 not boring movies`.
