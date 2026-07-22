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
   - [Day 2 Code Version](https://github.com/HamzaButt22/student-management-system/blob/132c0cd20482ce304093d2856d41c5ce0ec2038b/app.py) — Implemented class inheritance and runtime polymorphism via specialized student child structures.
   - [Day 3 Code Version](https://github.com/HamzaButt22/student-management-system/blob/4536bf0fe4e6c0f7332c5bd53c2115db28340c8e/app.py) — Integrated JSON serialization infrastructure to ensure database state persistence across application lifecycles.
   - [Day 4 Code Version](https://github.com/HamzaButt22/student-management-system/blob/7c4359c02708a308ed88fd78b1d5bde7157f4965/app.py) — Engineered descriptive class statistics modules combining custom manual loops with automated NumPy array verifications.
   - [Day 5 Code Version](https://github.com/HamzaButt22/student-management-system/blob/006396000ef5ef813510a03551aabb850e0efc8e/app.py) — Refactored variable namespaces, embedded formal internal function documentation docstrings, and deployed production-grade release architectures.

---

## Week 1

### Day 1 Milestone
- Set up the development environment using Anaconda and VS Code.
- Initialized Git tracking and linked the project to GitHub.
- Built a dictionary-based student record data model.

#### Features Built Day 1
- Dynamic user input handling for names, IDs, and GPAs.
- Structured data mapping using Python functions and dictionaries.

### Day 2 Milestone
- Extended the system to handle multiple records using lists and dictionaries.
- Modularized data entry and storage into a dedicated execution function.
- Engineered a clear terminal-based view function to display data collections.

#### Features Built Day 2
- Implemented a global list database to hold multiple records simultaneously.
- Created an iterative display process using clean text divider boundaries.

### Day 3 Milestone
- Implemented input validation for student records using string operations and conditional checks.
- Developed modular character and string scanning processes to catch edge-case entries.
- Created meaningful terminal error feedback tracking to handle bad input types gracefully.

#### Features Built Day 3
- Integrated strict length boundaries and alphabetical-space checks for names.
- Configured length constraints and digits-only isolation checking for ID numbers.
- Built comprehensive character analysis formatting to safely validate decimal float limits for GPAs.

### Day 4 Milestone
- Implemented a loop-driven menu system for adding, viewing, and searching student records.
- Restructured console mechanics to host persistent iterative selection execution.
- Designed a dynamic sequence lookup algorithm to fetch individual nested properties.

#### Features Built Day 4
- Engineered an infinite `while` loop operational workflow alongside terminal exit conditions.
- Implemented error-handling parameters for invalid option selections.
- Created a standalone sequence searching routine powered by localized search state flags.
- Built a duplicate detection guard clause to prevent redundant student ID registrations.

### Day 5 Milestone
- Refactored the program into modular functions and added exception handling for robustness.
- Isolated logical calculations from localized runtime operations.
- Engineered defensive type-casting filters using conditional trial procedures.

#### Features Built Day 5
- Structured dedicated `try/except` execution boundaries to intercept numerical value conversion failures.
- Prevented system crashes caused by invalid data types by routing runtime anomalies back to the main loop.
- Flattened programmatic function branching by eliminating deeply nested verification trees.

---

## Week 2

### Day 1 Milestone
- Converted the student management system to an object-oriented design using a Student class.
- Encapsulated core data fields and dynamic attributes within unique state parameters.
- Modularized record modification actions into specialized class methods.

#### Features Built Day 1
- Implemented class variable list states (`Student.student_database`) to anchor data arrays.
- Structured constructor engines (`__init__`) using implicit reference variables (`self`).
- Developed a safe record updater module (`Update_Student_Record()`) to alter parameters dynamically using explicit verification guards.

### Day 2 Milestone
- Implemented inheritance and polymorphism by extending the Student class into a GraduateStudent subclass.
- Designed hierarchical object structures allowing properties to flow seamlessly down to children templates.
- Overrode core display mechanisms to apply dynamic compilation layouts based on the target class type.

#### Features Built Day 2
- Structured the `GraduateStudent` subclass linked directly to the parent via Python's `super().__init__()` chain.
- Integrated a unique `thesis_topic` string attribute specialized for postgraduate record entities.
- Applied runtime polymorphism by overriding the instance `.display()` method across classes, removing manual formatting blocks from database lookup loops.
- Expanded the menu-driven routing engine with conditional query gates to determine student classifications prior to memory initialization.

### Day 3 Milestone
- Integrated JSON-based file persistence so student records are saved and reloaded correctly.
- Engineered automated serialization and deserialization data pipelines mapping custom class objects into native JSON streams.
- Configured defensive runtime error-catching boundaries to gracefully intercept data-stream disruptions.

#### Features Built Day 3
- Implemented `Save_To_JSON()` using Python's native `json.dump()` engine to parse in-memory object arrays into standard readable flat files.
- Built explicit attribute structural checking loops using `hasattr()` to isolate `GraduateStudent` specific fields before writing profiles to disk.
- Developed `Load_From_JSON()` wrapped inside structural `try/except` monitoring scopes to capture `FileNotFoundError` events smoothly during clean installations.
- Engineered a polymorphic type reconstruction module using key-membership testing (`if "thesis_topic" in data`) to dynamically map raw dictionaries back into standard or graduate object instances on startup.
- Fastened life-cycle operational hooks inside the terminal system, configuring boot-up database updates and immediate disk saving during application exit sequences.

### Day 4 Milestone
- Added a class statistics feature computing and verifying measures of central tendency and dispersion.
- Formulated native mathematical loop logic to process descriptive analytical summaries completely from scratch.
- Integrated parallel third-party math vectors to verify the accuracy of manual procedural operations.

#### Features Built Day 4
- Expanded terminal workspace option bounds to include a dedicated analytical summary selection feature.
- Built custom iterative calculation pipelines determining explicit data points for Arithmetic Mean, Minimum, and Maximum entries.
- Engineered median tracking systems handling conditional index evaluation splits for both even and odd total array populations.
- Developed frequency aggregation maps via native dictionary tracking to resolve dataset Mode targets manually.
- Programmed a step-by-step Standard Deviation calculator using variance squared deviations and fractional exponent root operations (`** 0.5`).
- Fastened side-by-side terminal verification reports printing manual output matrices next to built-in NumPy library functions (`np.mean`, `np.median`, `np.unique`, `np.std`).

### 🔹 Day 5 Milestone
- Polished architectural engine syntax and standardized code organization.
- Added comprehensive professional documentation to optimize the codebase for enterprise use.
- Isolated storage states from active tracking paths by formatting repository file boundaries.

#### Features Built Day 5
- Deployed comprehensive multi-line docstrings immediately underneath function declarations detailing argument parameters, element data types, and explicit return variables.
- Standardized runtime function scoping parameters and cleaned variable layouts across operational pipelines.
- Organized professional file tracking rules via local deployment configurations (`.gitignore`) to prevent test files from corrupting source environments.

---

## How to Run the Script
1. Ensure Python or Anaconda is installed.
2. Ensure you have the NumPy dependency package installed on your active environment:
   ```bash
   pip install numpy
   ```
3. Open your terminal in this directory.
4. Run the script:
   ```bash
   python3 app.py
   ```