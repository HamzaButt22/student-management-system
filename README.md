# student-management-system

A Python-based command-line tool designed to handle and organize student records efficiently.

## 📅 Project Version History
- **[Week 1]**
- [Day 1 Code Version](https://github.com/HamzaButt22/student-management-system/blob/76c0604d6e90ad75fb57c5a54248022312f789e5/app.py) — Initial single student data model script.
- [Day 2 Code Version](https://github.com/HamzaButt22/student-management-system/blob/56d74e21dfc9ba98a9571325261e108fffbc38f6/app.py) — Extended system handling multiple student records.
- [Day 3 Code Version](https://github.com/HamzaButt22/student-management-system/blob/68a9b1843cb6aeeb1a76ff5c9bad365660cd42ac/app.py) — Added input validation using string methods and conditional checks.
- [Day 4 Code Version](https://github.com/HamzaButt22/student-management-system/blob/a124fbc464e72a59a49117d82b41201a511b9eb2/app.py) — Implemented a loop-driven interactive terminal menu with search functionality and data-integrity guards.
- [Day 5 Code Version](https://github.com/HamzaButt22/student-management-system/blob/48a0ac8c46829f96a6b157c86a2c53be889cf75a/app.py) — Refactored application code into modular architectures and integrated standard exception handling layers.
- **[Week 2]**
- [Day 1 Code Version](https://github.com/HamzaButt22/student-management-system/blob/91cea2c4e50e5b72d527846fa2999cc80364e554/app.py) — Migrated system infrastructure to Object-Oriented Programming (OOP) using custom Student entity blueprints.

## Week 1

## Day 1 Milestone
- Set up the development environment using Anaconda and VS Code.
- Initialized Git tracking and linked the project to GitHub.
- Built a dictionary-based student record data model.

## Features Built Day 1
- Dynamic user input handling for names, IDs, and GPAs.
- Structured data mapping using Python functions and dictionaries.

## Day 2 Milestone
- Extended the system to handle multiple records using lists and dictionaries.
- Modularized data entry and storage into a dedicated execution function.
- Engineered a clear terminal-based view function to display data collections.

## Features Built Day 2
- Implemented a global list database to hold multiple records simultaneously.
- Created an iterative display process using clean text divider boundaries.

## Day 3 Milestone
- Implemented input validation for student records using string operations and conditional checks.
- Developed modular character and string scanning processes to catch edge-case entries.
- Created meaningful terminal error feedback tracking to handle bad input types gracefully.

## Features Built Day 3
- Integrated strict length boundaries and alphabetical-space checks for names.
- Configured length constraints and digits-only isolation checking for ID numbers.
- Built comprehensive character analysis formatting to safely validate decimal float limits for GPAs.

## Day 4 Milestone
- Implemented a loop-driven menu system for adding, viewing, and searching student records.
- Restructured console mechanics to host persistent iterative selection execution.
- Designed a dynamic sequence lookup algorithm to fetch individual nested properties.

## Features Built Day 4
- Engineered an infinite `while` loop operational workflow alongside terminal exit conditions.
- Implemented error-handling parameters for invalid option selections.
- Created a standalone sequence searching routine powered by localized search state flags.
- Built a duplicate detection guard clause to prevent redundant student ID registrations.

## Day 5 Milestone
- Refactored the program into modular functions and added exception handling for robustness.
- Isolated logical calculations from localized runtime operations.
- Engineered defensive type-casting filters using conditional trial procedures.

## Features Built Day 5
- Structured dedicated `try/except` execution boundaries to intercept numerical value conversion failures.
- Prevented system crashes caused by invalid data types by routing runtime anomalies back to the main loop.
- Flattened programmatic function branching by eliminating deeply nested verification trees.

## Week 2

## Day 1 Milestone
- Converted the student management system to an object-oriented design using a Student class.
- Encapsulated core data fields and dynamic attributes within unique state parameters.
- Modularized record modification actions into specialized class methods.

## Features Built Day 1
- Implemented class variable list states (`Student.student_database`) to anchor data arrays.
- Structured constructor engines (`__init__`) using implicit reference variables (`self`).
- Developed a safe record updater module (`Update_Student_Record()`) to alter parameters dynamically using explicit verification guards.

## How to Run the Script
1. Ensure Python or Anaconda is installed.
2. Open your terminal in this directory.
3. Run the script:
   ```bash
   python3 app.py
   ```