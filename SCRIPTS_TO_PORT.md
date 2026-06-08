# Week 1 — Python Warm-Up Utilities

Three stdlib-only utilities to build Python fluency. No external libraries
(no pandas) — the point is to learn core Python idioms first. Public-domain
data only.

Suggested order: CSV transformer → word-frequency counter → log parser.

---

## 1. CSV Transformer  (do this first)

**Task:** Read a CSV, clean it, add derived columns, write it back out.
- Strip whitespace from string fields
- Coerce numeric columns to int/float; handle blanks/missing gracefully
- Drop or flag rows with missing critical values
- Add at least one derived column (e.g. a computed or categorized field)
- Write the cleaned result to a new CSV

**Data:** Titanic dataset (small, public domain, mixed types + missing values).
- https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- Alternative: Iris dataset (even smaller, all numeric + one text label).

**Teaches:** `csv` module (reader/DictReader, writer/DictWriter),
type coercion, handling missing values, list/dict comprehensions,
`dataclasses` for a typed row.

---

## 2. Word-Frequency Counter  (do this second)

**Task:** Read a text file, normalize it, output a ranked word-frequency list.
- Lowercase, strip punctuation
- Split into words
- Count occurrences, print top N (e.g. top 20)
- Optional: ignore common stop-words (the, a, and, of...)

**Data:** Project Gutenberg (public domain books, plain text).
- Pride and Prejudice: https://www.gutenberg.org/files/1342/1342-0.txt
- Moby Dick: https://www.gutenberg.org/files/2701/2701-0.txt

**Teaches:** file reading, string normalization, `collections.Counter`,
`str.translate`/`str.maketrans` for punctuation, sorting with key functions.

---

## 3. Log-Line Parser  (do this third)

**Task:** Parse log lines into structured records, then summarize:
- Count lines by level (INFO / WARN / ERROR)
- Find the busiest hour
- Show the top 5 most frequent messages

**Data:** Generate synthetic logs yourself (a ~15-line generator script that
writes random timestamps + levels + messages to a file). Generating realistic
test data is itself a useful DE skill.
- Alternative (real logs): Loghub — https://github.com/logpai/loghub

**Teaches:** `dataclasses`, `collections.Counter` / `defaultdict`,
`datetime` parsing, string splitting, generating test data.

---

## Definition of done (week 1)
- [ ] All three run from the command line on real input
- [ ] Each has at least 2-3 pytest tests
- [ ] `ruff check .` passes clean
- [ ] Pushed to GitHub