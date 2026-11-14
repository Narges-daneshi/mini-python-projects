# Expense Tracker 💰

A simple command-line application built with Python to track daily expenses, manage spending records, and generate expense reports.

## Features

- **Add Expense:** Record a new expense with a title, amount, category, and automatically assigned date.
- **Show Expenses:** Display all recorded expenses with their details.
- **Show Total:** Calculate the total amount of all expenses.
- **Delete Expense:** Remove an expense by selecting its number.
- **Filter by Category:** Find expenses belonging to a specific category (case-insensitive).
- **Category Report:** Calculate and display the total spending for each category.
- **Monthly Report:** Group expenses by year and month and calculate monthly spending.

## How to Run

1. Make sure Python is installed on your system.
2. Clone the repository:

   ```bash
   git clone https://github.com/Narges-daneshi/mini-python-projects.git
   ```

3. Navigate to the project directory:

   ```bash
   cd mini-python-projects/beginner/expense-tracker
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## Concepts Practiced

- Functions and modular programming
- Lists and dictionaries
- List comprehensions
- Dictionary aggregation using `dict.get()`
- Exception handling (`try` / `except`)
- Input validation
- Date and time handling with the `datetime` module
- Built-in functions such as `sum()` and `enumerate()`
- Loops and conditional statements

## Limitations

- Expenses are stored in memory and are not saved after the program exits.
- Expense amounts are limited to integers.
- The application uses the system's current date when adding a new expense.
