# SQL practice

Daily SQL questions for data analyst and data engineering roles. Every question is one `.sql` file: the task, the source link, the expected result, a runnable sample table and a place for your answer.

## Folders

| Folder | What it holds |
| --- | --- |
| [`easy/`](easy/README.md), [`medium/`](medium/README.md), [`hard/`](hard/README.md) | Assigned questions, stored once under their LeetCode difficulty |
| `easy_solved/` | Questions already solved. Move a file here when it is done |

Question numbers are one sequence for the whole SQL track and keep counting across difficulty levels. The number in the file name is this repo's own counter; the source platform's problem ID is inside the file.

```text
sql/
├── easy/             assigned easy questions + index
├── easy_solved/      finished easy questions
├── medium/           assigned medium questions + index
└── hard/             assigned hard questions + index
```

## Run a question

Each file creates its own sample tables. Write your query under `-- YOUR ANSWER`, then run it in a fresh SQLite session:

```sh
cd sql
sqlite3
.headers on
.mode column
.read easy/10_not_boring_movies.sql
.quit
```

On LeetCode, paste only your answer query, not the setup. The files target ANSI/PostgreSQL SQL and the setup also runs in SQLite. Dialects differ, for example `CHAR_LENGTH(content)` in PostgreSQL and `LENGTH(content)` in SQLite, so pick the dialect before you run.

## Commit your work

Example message: `practice: solve question 10 not boring movies`

## Routine

Monday to Friday at 19:00 (Europe/Berlin), 5 SQL questions. Difficulty rises with reviewed work, and earlier questions come back for recall.
