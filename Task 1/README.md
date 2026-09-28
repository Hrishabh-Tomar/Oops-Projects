# Student Management System (Python OOP)

A small command-line Student Management System that shows the core ideas of Object-Oriented Programming in Python: classes, objects, constructors, instance methods, class variables and class methods.

## Features

- Create student records with name, email, student ID, course and marks
- Show a student's full details
- Add or update marks for a subject, with a check that the score is between 0 and 100
- Work out a student's average marks
- Count the total number of students with a class variable and a class method

## OOP Concepts Covered

| Concept | Implementation |
|---|---|
| **Class** | `Student` |
| **Objects** | `s1`, `s2`, `s3`, three separate student instances |
| **Constructor (`__init__`)** | Sets `name`, `email`, `student_id`, `course`, `marks` |
| **Instance methods** | `display_details()`, `update_marks()`, `calculate_average()` |
| **Class variable** | `total_students` is shared by all instances and goes up by 1 each time a student is created |
| **Class method** | `@classmethod get_total_students()` |

## Project Structure

```
.
├── student_management.py   # Student class + demo
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

Open a terminal in the project folder, then run:

```bash
# Mac / Linux
python3 student_management.py

# Windows
python student_management.py
```

## Usage Example

```python
from student_management import Student

s1 = Student("Aarav Sharma", "aarav@example.com", "S101", "Data Science",
             {"Python": 88, "Statistics": 76})

s1.display_details()                 # print all details
s1.update_marks("Statistics", 84)    # update an existing subject
s1.update_marks("SQL", 91)           # add a new subject
print(s1.calculate_average())        # 87.67

print(Student.get_total_students())  # total students created
```

## Sample Output

```
=== Updating Marks ===
Updated Statistics for Aarav Sharma: 76 -> 84
Added Python: 90 for Rohan Mehta
Added Java: 78 for Rohan Mehta
Invalid score 105. Marks must be between 0 and 100.

=== Averages After Update ===
Aarav Sharma    -> 87.67
Priya Verma     -> 79.00
Rohan Mehta     -> 84.00

=== Class Method ===
Total students: 3
```

## Method Reference

| Method | Type | Description |
|---|---|---|
| `__init__(name, email, student_id, course, marks=None)` | Constructor | Creates a student and increases `total_students` by 1 |
| `display_details()` | Instance | Prints the student's details, marks and average |
| `update_marks(subject, new_score)` | Instance | Adds or updates a subject score from 0 to 100 and refuses anything outside that range |
| `calculate_average()` | Instance | Returns the average of all marks, or `0.0` if there are no marks |
| `get_total_students()` | Class | Returns the total number of students created |

## Possible Enhancements

- Delete or search students by ID
- Save records to a CSV or JSON file
- Add a menu-driven CLI so users can enter data interactively
- Assign grades based on the average
