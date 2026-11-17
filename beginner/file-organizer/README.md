# File Organizer 📁

## Overview

A Python script that automatically organizes files in a selected directory into separate folders based on their file extensions.

## Features

- Automatically creates category folders.
- Organizes files based on their extensions.
- Supports images, documents, audio, videos, code files, and archives.
- Handles duplicate filenames by asking the user whether to replace or skip the existing file.
- Displays a summary of moved, replaced, and skipped files.
- Validates the selected directory path.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Narges-daneshi/mini-python-projects.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mini-python-projects/beginner/file-organizer
   ```

3. Run the script:

   ```bash
   python main.py
   ```

4. Enter the directory path you want to organize.

## Concepts Practiced

- Working with `pathlib` for file and directory management.
- Using `shutil` to move files.
- Using `os.replace()` to replace existing files.
- Working with file extensions and paths.
- Creating directories programmatically.
- Iterating over directory contents.
- Handling duplicate files.
- Using functions, dictionaries, sets, and loops.

## Limitations

- Only organizes files directly inside the selected directory, not files in subdirectories.
- Files with unsupported extensions remain in the original directory.
- Files are moved rather than copied.
- Replacing an existing file permanently overwrites the previous file.

