# Sovereign-Python-Fleet 🛡️

**A learning repository showcasing Python fundamentals and a real-world business automation project.**

---

## Repository overview

This repo contains a series of short learning projects (1–12) that demonstrate core Python concepts, plus a final real-world automation project that cleans invoice data, deduplicates entries, calculates tax, and writes a financial report to disk.

Files of note:

- `Business Data Cleaner Project .py` — Project 13: the main real project (invoice cleaning, validation, tax calculation, file output).
- `File read & creation And try & except, Last learning Project .py` — Example of file I/O and try/except handling.
- Other learning projects (loops, lists, dicts, sets, functions, etc.) named `*.py` in the root.

---

## 📚 Projects

### Learning Projects (Fundamentals)
Short practice scripts that teach the basics:
- Loops, conditionals, and branching
- Functions and simple modular code
- Data structures: lists, dicts, sets, tuples
- File I/O and basic error handling
- Small algorithmic problems and practice exercises
- Total Projects: 19 Projects

These are small, self-contained files you can run directly with Python for quick practice.

### Real Project — Project 13: Business Data Cleaner & Ledger Automator ⭐
- **Purpose:** Clean raw invoice data (remove duplicates and malformed rows), calculate aggregates (totals, per-client revenue), compute tax, and export a summarized report to a text file.
- **Skills demonstrated:** data validation, duplicate detection, use of lists/dicts/sets, error handling, file operations, basic automation logic.
- **Main file:** `Business Data Cleaner Project .py`
- **Run:**

```bash
python "Business Data Cleaner Project .py"
```

The script prints a financial summary and writes `sovereign_financial_report.txt` to the repository folder.

---

## 🛠️ Optional: Add SQL Integration (recommended next step)
If you want to extend the project and show SQL skills (recommended for job openings that ask for Python + SQL), you can add a simple SQLite integration:
- Create `sovereign.db` with an `invoices` table
- Insert the raw invoice list into the table
- Use SQL queries (GROUP BY, SUM, DISTINCT) to detect duplicates and compute aggregates
- Export a report using Python + sqlite3

This is a great addition to your portfolio because many employers look for SQL basics (SELECT, GROUP BY, JOINs, aggregates).

---

## 🎯 Key Features (what employers see)
- Duplicate invoice detection and removal
- Data validation (catches malformed entries gracefully)
- Automated tax calculation and net profit computation
- Report generation (writes to `sovereign_financial_report.txt`)
- Demonstrates ability to think through a business problem and implement a working automation

---

## 🚀 Getting Started (quick)
1. Clone the repo

```bash
git clone https://github.com/blackk56/Sovereign-Python-Fleet.git
cd Sovereign-Python-Fleet
```

2. Make sure you have Python installed (3.8+ recommended)
3. Run the main project

```bash
python "Business Data Cleaner Project .py"
```

4. Check the generated `sovereign_financial_report.txt` for output

---

## 📝 Notes on style and polish
- The code uses clear comments and section headers to explain each step. Consider these quick polish steps before applying to jobs:
  - Rename files to remove spaces if you prefer (e.g., `business_data_cleaner.py`).
  - Add small docstrings to functions and the top of scripts.
  - Add a short `requirements.txt` if you later use external libraries.

---

## 💡 What I learned building this repo
- How to design a small automation pipeline: read -> clean -> calculate -> report
- Practical handling of corrupt input using try/except
- File read/write patterns and Python data structures for deduplication
- How to prepare a small project for a portfolio and explain it clearly

---

## 📧 Contact / Job preferences
Looking for junior Data Analyst roles (remote required), Skills; Python & MySQL, Please reach out via GitHub or email

---

**Status:** 30 days of Python learning → First real project completed ✅
