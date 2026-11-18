# Log Analyzer 📊

A command-line application built with Python to parse, validate, analyze, and filter server log files. It generates statistical summaries, identifies frequently occurring error messages, and saves the analysis results in a text report.

## Overview

Log Analyzer reads server log files line by line, validates their structure and content, and extracts useful information from valid entries.

It provides statistics about log levels, identifies the most common error messages, and allows users to filter logs by severity level and time range.

The project also includes a sample log file (`server.log`) containing valid and invalid entries for testing the application.

## Features

- **Log Parsing:** Reads log files line by line and extracts timestamps, log levels, and messages.
- **Input Validation:** Validates timestamps, supported log levels (`INFO`, `WARNING`, `ERROR`), and log messages.
- **Entry Statistics:** Counts total, valid, and invalid log entries.
- **Log Level Analysis:** Calculates the number of entries for each log level.
- **Error Analysis:** Identifies frequently occurring error messages and ranks them by frequency.
- **Level-Based Filtering:** Filters log entries by their severity level.
- **Time-Based Filtering:** Filters logs within a user-defined date and time range.
- **Report Generation:** Displays analysis results in the terminal and saves them to a text report.
- **File Handling:** Handles missing input files by prompting the user to provide another file path.

## Project Structure

```text
log-analyzer/
├── main.py
├── server.log
└── report.txt  (generated automatically)
```

- `main.py`: Contains the application logic.
- `server.log`: Sample input file containing server log entries.
- `report.txt`: Generated report containing analysis statistics and filtered log entries.

## Log File Format

The application expects each log entry to follow this format:

```text
YYYY-MM-DD HH:MM:SS LOG_LEVEL Message
```

Example:

```text
2026-11-19 08:10:00 ERROR Database timeout
2026-11-19 08:15:00 WARNING High CPU usage
2026-11-19 08:20:00 INFO Request completed
```

Supported log levels:

- `INFO`: Informational messages.
- `WARNING`: Potential issues that may require attention.
- `ERROR`: Error events that indicate a problem.

Entries with invalid timestamps, unsupported log levels, or empty messages are considered invalid.

## Requirements

- Python 3.8 or higher
- No external libraries required.

The project uses Python's built-in `datetime` module for parsing and comparing timestamps.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Narges-daneshi/mini_python_projects.git
```

2. Navigate to the project directory:

```bash
cd mini_python_projects/beginner/log-analyzer
```

3. Run the application:

```bash
python main.py
```

4. Enter a log level when prompted:

```text
INFO
WARNING
ERROR
```

5. Enter the start and end timestamps using the following format:

```text
YYYY-MM-DD HH:MM:SS
```

The application displays the analysis results in the terminal and generates a `report.txt` file in the current working directory.

## Concepts Practiced

- File handling and reading files line by line
- String manipulation and parsing
- Exception handling (`try`, `except`)
- Input validation
- Working with the `datetime` module
- Lists and dictionaries
- Dictionary methods (`get()`)
- Sorting with custom keys (`sorted()` and `lambda`)
- Iteration and conditional statements
- Writing structured reports to text files
- Modular programming and function design

## Limitations

- Supports only the predefined log levels: `INFO`, `WARNING`, and `ERROR`.
- Expects timestamps in the `YYYY-MM-DD HH:MM:SS` format.
- Uses a predefined log structure and does not support arbitrary log formats.
- Processes one log file per execution.
- Generates a plain text report rather than a graphical dashboard.
- The time filter is applied to the logs already filtered by severity level.

## Future Improvements

Possible extensions for this project include:

- Supporting additional log levels and formats.
- Adding command-line arguments for file paths and filtering options.
- Supporting multiple log files.
- Generating reports in CSV or JSON format.
