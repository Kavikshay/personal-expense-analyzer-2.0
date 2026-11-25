# Personal Expense Analyzer 2.0

A Python-based Personal Expense Analyzer that helps users manage, track, and analyze their daily expenses using CSV files. It also supports JSON data conversion and importing.

## Features

- **Add New Expenses:** Record expenses with date, month, year, item name, description, and amount.
- **View All Expenses:** Display all stored expense records.
- **Expense Analysis:** Calculate total spending for each item.
- **Search Expenses:** Search expenses by date, month, or year.
- **Find Highest Expense:** Identify the highest individual expense.
- **Monthly Expense Report:** Generate monthly reports showing total expenses and transaction counts.
- **Top 5 Expenses:** Display the five items with the highest accumulated spending.
- **CSV to JSON:** Convert CSV expense records into JSON format.
- **JSON to CSV:** Import JSON records into the CSV expense file.

## Technologies Used

- Python 3
- CSV module
- JSON module
- OS module
- pathlib module

## Python Concepts Practiced

- Functions
- Lists and Dictionaries
- File Handling
- Exception Handling
- CSV Reading and Writing
- JSON Serialization and Deserialization
- Sorting and Lambda Functions
- Data Analysis

## Project Structure

```text
Personal-Expense-Analyzer-2.0/
│
├── main.py
├── README.md
├── .gitignore
└── Personal Expense data.example.csv
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Create a working CSV file named `Personal Expense data.csv` using the example CSV template.
4. Open the project folder in VS Code.
5. Run the following command:

```bash
python main.py
```

## CSV Data Format

The expense CSV file uses the following columns:

- date
- month
- year
- name
- description
- amount

## JSON Support

The project supports converting expense records between CSV and JSON formats.

JSON data is stored using Python's built-in JSON module.

## Learning Purpose

This project was developed as part of my Python learning journey to practice file handling, data management, CSV operations, JSON operations, and exception handling.

It is an improved version of my earlier Personal Expense Analyzer project.

---

**Project:** Personal Expense Analyzer 2.0  
**Language:** Python  
**Version:** 2.0
