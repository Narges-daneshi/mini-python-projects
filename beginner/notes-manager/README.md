Notes Manager 📝 

A simple command-line Notes Manager built with Python. It allows users to create, view, search, and delete notes while storing them persistently in a JSON file.

Features

- Add Notes: Create notes with a title and content.
- Show Notes: Display all saved notes.
- Search Notes: Find notes by searching keywords in their titles or content.
- Delete Notes: Remove notes by selecting their number.
- Data Persistence: Automatically save and load notes using a JSON file.
- Input Validation: Prevent empty inputs and handle invalid selections.
- JSON Validation: Check the structure and data types of loaded notes.

How to Run

1. Clone the repository:
   
   git clone https://github.com/Narges-daneshi/mini-python-projects.git

2. Navigate to the project directory:
   
   cd mini-python-projects/beginner/notes-manager

3. Run the program:
   
   python main.py

The program automatically creates and updates "notes.json" when notes are added or deleted. A sample "notes.json" file is also included.

Concepts Practiced

- Python Functions
- Lists and Dictionaries
- Loops and Conditional Statements
- String Methods
- List Manipulation
- Exception Handling
- File Handling
- JSON Serialization and Deserialization
- Input Validation
- Data Persistence

Limitations

- Notes are stored locally in a JSON file.
- The application runs in the command line.
- Notes cannot be edited after creation.
- If the JSON file contains invalid data, the program starts with an empty notes list.
