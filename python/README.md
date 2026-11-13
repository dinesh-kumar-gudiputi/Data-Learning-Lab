# Python Daily Coding

Focused Python problem-solving practice for data analyst and data engineering roles. This repository contains only daily coding questions and your attempts.

## Structure

```text
PYTHON/
├── README.md
├── easy/
├── medium/
└── hard/
```

| Difficulty | Questions |
| --- | --- |
| Easy | [Open easy questions](easy/README.md) |
| Medium | [Open medium questions](medium/README.md) |
| Hard | [Open hard questions](hard/README.md) |

Each question is stored **once**, under its LeetCode difficulty. Easy, medium and hard contain different questions, not three versions of the same question. A retry stays with the original file.

## File names

Start question numbering at 1 and continue within this repository, followed by the question name:

```text
easy/1_contains_duplicate.py
```

The filename number is your own question sequence. PYTHON and SQL each have an independent counter. Continue the counter across easy, medium and hard; do not restart it when changing difficulty. Keep the source platform's problem ID in the file's source information. There are no date folders. New question files contain the task, source link, example and starter code. The current starter files are intentionally unimplemented.

## Start in VS Code

1. In VS Code, run **Git: Clone** and use `https://github.com/dinesh-kumar-gudiputi/PYTHON.git`, or open the local PYTHON folder yourself.
2. Open the assigned numbered file under `easy/`, `medium/` or `hard/`.
3. Write your own attempt, check the examples and edge cases, then submit it to the mentor for review.
4. In **Source Control**, review and stage the question files you changed.
5. Enter a clear commit message, commit, then use **Push** or **Sync Changes**.

When both daily repositories are open, select the matching repository in Source Control before committing. The mentor does not automatically upload your daily solutions.

Example commit: `practice: solve question 1 contains duplicate`

## First prepared questions

| Number | Question file |
| --- | --- |
| 1 | [Contains Duplicate](easy/1_contains_duplicate.py) |
| 2 | [Valid Anagram](easy/2_valid_anagram.py) |
| 3 | [Move Zeroes](easy/3_move_zeroes.py) |

## Run your code

Use Python 3 and the VS Code Python extension. An optional `.venv` keeps dependencies separate. The first questions need only the standard library.

Function stubs raise `NotImplementedError` until you implement them. A file that only defines functions needs you to call those functions with the examples or add your own tests; running the file alone does not test the solution.

## Weekday training

The coding chat runs Monday–Friday at **19:00 Europe/Berlin**, with 3 Python questions. Difficulty increases based on reviewed work, with later recall of earlier questions. Approximately 90 minutes for both languages together is a flexible target.

Questions and starter files can be prepared in the local checkout. Your own reviewed attempts are committed and pushed by you.
