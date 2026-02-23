# Assessment 004 - Summative

## Learning Outcomes assessed

- Data Structures
- Data Manipulation
- String Formatting
- Loops
- CLI Commands
- APIs

--

## Assessment Structure

The following Assessment has two sections:

- [Coding Assessment (Questions are below)](#fundamentals-coding-assessment)
- [Long Questions (Questions are below)](#long-format-questions) - `answers.txt`

You can answer them in any order.


## Your Goal

Read the instructions below for each [coding question](#fundamentals-coding-assessment), then complete each function in `data_structures.py` while ensuring that:

- The code is valid Python
- Each function behaves according to the instructions
- All unit tests pass successfully

Read the instructions below for each [long format question](#long-format-questions), then add your answer under each relevant comment in `answers.txt` while ensuring thatL

- You DO NOT remove the comments
- Read each question carefully before answering the question

---

### How to run your tests

To run all your tests

```bash
python3 -m pytest tests/test_summative.py -v
```

To run your tests individually

```bash
python3 -m pytest tests/test_summative.py::<test_method> -v
```

or for more information within the stacktace use

```bash
python3 -m pytest tests/test_summative.py::<test_method> -vv
```

## Scoring & Weighting

| Component                                     | Weight  |
| --------------------------------------------- | ------- |
| Coding Section (unit tests)                   | **50%** |
| Long-format Question (answers.txt)            | **50%** |


--

## Fundamentals Coding Assessment

This assessment consists of five Python functions. Each function has a partially written
implementation. Your task is to **fix the bugs**, **complete the missing logic**, and **ensure all tests pass**.

### Project Structure

```text
fun-004-summative/
├── summative.py              # <-- This is where you write your solutions
├── answers.txt                     # <-- This is where you write your answers to the long questions
├── tests/
│   └── test_summative.py     # <-- These are the tests you must make pass
└── README.md                       # <-- Assessment instructions (this file) 
```

### Question 1 - `batch_api_dispatcher(user_ids)`

The South African Social Security Agency (SASSA) needs to send out SMS notifications to citizens regarding their grant statuses. To keep the government servers running smoothly and avoid "crashing" the system, the SMS gateway has a strict limit: *it can only process a maximum of 5 users at a time in a single "batch" request*.

You have a list of `user_ids` that need their notifications sent. Your job is to help the IT team at the department in *Pretoria* organise these IDs into smaller groups (sublists) so the system can process them without any errors.

Apply your logic to the `batch_api_dispatcher()` function. The function should take the full list of IDs and break them down into a nested list where each internal "batch" contains a maximum of 5 IDs. If the total number of users isn't a perfect multiple of 5, the final batch will simply contain the remaining IDs.

- **Input:**

```python
['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7']
```

- **Output:**

```python
[['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6', 'ID7']]
```

Constraint: No sublist should ever exceed 5 items.


### Question 2 - `winning_streak(streak)`

The Springboks are on a world tour, and the whole of South Africa is wearing their green and gold jerseys every Friday. From Loftus Versfeld to Twickenham, the fans are tracking every single match.

The South African Rugby Union (SARU) wants to update their website with a "Longest Winning Streak" stat to show just how dominant the team has been. They have a list of results where "W" stands for a glorious win and "L" stands for a tough loss. They need you to look through the season's history and find the highest number of consecutive wins (wins in a row).

Apply your logic to the `winning_streak()` funciton which analyses a list of game results. The function must count how many times "W" appears in a row and return the highest count found.

- **Input:** A list of strings (e.g., ["W", "L", "W", "W", "L", "W", "W", "W"])
- **Output:** An integer representing the longest streak (e.g., 3)

---

### Question 3 - `peak_finder(temperatures)`

The South African Weather Service (SAWS) is monitoring a massive heatwave moving across the Northern Cape. In towns like Upington, the temperature can climb incredibly high, but it often fluctuates.

A "Local Peak" occurs when one day is hotter than the day before it and the day after it. The weather station has sent you a list of maximum temperatures (in degrees Celsius) recorded over the last few weeks. To help farmers prepare for the hottest spikes, you need to identify every "Peak Temperature" in the sequence.

Apply your logic to the `peak_finder()` function which looks through the list of temperatures. It should identify any temperature that is strictly greater than the one immediately before it and the one immediately after it.

- **Input:** A list of integers (e.g., [30, 32, 31, 35, 33, 36, 34, 38, 37, 39, 35, 40, 38, 37, 36, 35, 34, 33, 32, 31, 30])
- **Output:** A list of the identified peak temperatures (e.g., [32, 35, 36, 38, 39, 40])

---


### Question 4 - `stage_summary(records)`

Eskom's public API has been down for weeks, but a junior developer on your team managed to pull a snapshot of load shedding incident data before it went offline. The data has been saved locally as `loadshedding.json` — a list of incidents recorded across South African suburbs, each showing which load shedding stage was active and for how long.

Your team lead needs a quick report: **how many total hours was each stage active, across all areas and all dates?**

Apply your logic to the `stage_summary()` function. It receives the list of incident records (already loaded from the JSON) and must return a dictionary where each key is a stage label (`"Stage 1"`, `"Stage 2"`, etc.) and each value is the **total hours** recorded for that stage — rounded to 2 decimal places.

Only include stages that actually appear in the data. If the input is empty, return an empty dictionary.

- **Input:** A list of incident dictionaries, e.g.:
```python
[
    {"incident_id": "ESK-20240601-001", "area": "Soweto", "municipality": "City of Johannesburg", "province": "Gauteng", "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00", "end_time": "08:30", "status": "resolved", "scheduled": true, "affected_customers": 14200},
    {"incident_id": "ESK-20240601-002", "area": "Sandton", "municipality": "City of Johannesburg", "province": "Gauteng", "stage": 4, "duration_hours": 4.0, "date": "2024-06-01", "start_time": "08:00", "end_time": "12:00", "status": "resolved", "scheduled": true, "affected_customers": 8750}
]
```

- **Output:**
```python
{"Stage 2": 2.5, "Stage 4": 4.0}
```

> **Note:** The order of keys in the returned dictionary does not matter. Your function only needs the `stage` and `duration_hours` fields — the rest of the data is there for context.


### Question 5 - `draw_triangle(height)`

The Drakensberg Hiking Club is building a small terminal app to generate trail difficulty badges for their members. Each badge displays a hollow triangle — the taller the triangle, the harder the trail.

Your job is to generate the badge shape. Apply your logic to the `draw_triangle()` function which takes a single integer `height` and returns a **list of strings**, where each string is one row of a hollow isosceles triangle made of `*` characters.

#### Rules:
- The triangle must be **centred** — each row is padded with leading spaces so the peak sits at the top centre.
- The **first row** has exactly one `*`.
- All **middle rows** have exactly two `*` characters with spaces in between.
- The **last row** is solid — filled entirely with `*` characters.
- If `height` is `1`, the triangle is just a single `*`.
- The **total width** of every row must be the same: `2 * height - 1`.

- **Input:** `5`
- **Output:**
```python
[
    "    *    ",  # ← wrong, width should be 2*5-1 = 9
]
```

Wait — let me show this properly:
```
height = 5
```
```
    *
   * *
  *   *
 *     *
*********
```

Returned as:
```python
[
    "    *",
    "   * *",
    "  *   *",
    " *     *",
    "*********"
]
```

> **Note:** Trailing spaces are optional — rows do not need to be padded on the right.


## Long-Format Questions


### Comprehension Question 1 — Linux Navigation & File Management (10 Points)

You have just been given access to a remote Linux server at a fintech company in Sandton. Your manager has given you the following tasks to complete:

1. See what files and folders are currently on the server
2. Move into a folder called `config`
3. Read the contents of a file called `settings.conf`
4. Create a new folder called `backup`
5. Make a copy of `settings.conf` and put it in the `backup` folder
6. Delete an old file called `server.log`

Describe **exactly how you would complete each task** — what command you would use, what it does, and why you chose it. Also explain any risks involved in any of your steps and how you would handle them carefully.


### Comprehension Question 2 — Loops (10 Points)

A junior developer on your team at a Cape Town startup keeps writing code that works but uses the wrong loop for the job. Your tech lead has asked you to sit down with them and explain how loops work and how to decide which one to reach for.

In your own words, explain loops to this junior developer. Your explanation should cover what the different types of loops are, how they work, and most importantly how a developer decides which one to use in a given situation. Make sure your explanation is grounded in realistic situations a developer might actually find themselves in, not just theory.



### Comprehension Question 3 — Immutable Data Types (10 Points)

During a code review at a Johannesburg dev agency, a senior engineer flags your colleague's code and says: *"You're treating this string like it's a list — that's not how Python works."* Your colleague has no idea what the engineer means and pulls you aside to ask for help.

Explain to your colleague what immutable data types are in Python, why they matter, and how Python actually behaves when a developer tries to change something that cannot be changed. Make sure your explanation helps them understand which types in Python are immutable, how this is different from types that can be changed, and the real practical implications this has when writing and debugging code.


### Comprehension Question 4 — APIs and HTTP

During your first week at a software company in Johannesburg, a non-technical product manager pulls you into a meeting and asks you to explain how the company's mobile app actually talks to the server. They've heard the word "API" thrown around constantly but have no idea what it means or how it works.

Explain APIs to this product manager in a way they can genuinely follow. Your explanation should cover what an API actually is and the role it plays, how the web communicates using HTTP, the different types of requests a client can make to a server and what each one is used for, and what an endpoint is and how it fits into the picture. You are welcome to use analogies to make your explanation clearer.