# Contact Book 📒

## Overview
A simple command-line Contact Book application written in Python. It allows users to manage their contacts by adding, displaying, searching, and deleting contact information.

## Features
- Add new contacts with name, phone number, and email address.
- Validate user input:
  - Names cannot be empty.
  - Phone numbers must contain exactly 11 digits and start with `09`.
  - Email addresses are checked using Regular Expressions.
- Display all saved contacts with numbered entries.
- Search for contacts by name (case-insensitive).
- Delete contacts by name (case-insensitive).
- Handle invalid inputs and empty contact lists.

## How to Run

1. Make sure Python is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Narges-daneshi/mini-python-projects.git
   ```
3. Navigate to the project directory:
   ```bash
   cd mini-python-projects/beginner/contact-book
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Concepts Practiced
- Functions and function parameters
- Lists and dictionaries
- Loops and conditional statements
- Input validation
- String methods (`strip()`, `lower()`, `isdigit()`, `startswith()`)
- List iteration with `enumerate()`
- List manipulation (`append()`, `pop()`)
- Regular Expressions (`re` module)
- `for...else` statements

## Limitations
- Contacts are stored in memory and will be lost when the program exits.
- Each contact is identified and searched by name.
