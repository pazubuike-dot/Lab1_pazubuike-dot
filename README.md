# Lab 1: Grade Evaluator & Archiver

## Description
This project consists of a Python application that evaluates student grades from a CSV file and a Bash script that archives the data.

## How to Run
1. Python Script:
   - Ensure `grades.csv` is in the directory.
   - Run the command: `python3 grade-evaluator.py`
   - Enter `grades.csv` when prompted.

2. Bash Script:
   - Give execution permissions: `chmod +x organizer.sh`
   - Run the script: `./organizer.sh`

## Features
- [cite_start]**Validation**: Checks if scores are 0-100 and weights total 100 (60 Formative / 40 Summative)[cite: 33, 34, 35].
- [cite_start]**GPA**: Calculates GPA on a 5.0 scale.
- [cite_start]**Archiving**: Moves processed grades to an `archive/` folder with a timestamp[cite: 51].
