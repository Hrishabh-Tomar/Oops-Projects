# Task 7: Super30 Learning Platform – OOP Capstone (Python)

The main assignment, combining every OOP concept from tasks 1–6. It is a mini learning platform where students register, enroll in courses, get assigned mentors and submit assignments. Mentors manage a limited number of students each.

```
User
 |
 +---- Student   (course, completed assignments)
 |
 +---- Mentor    (expertise, assigned students)
```

## Features

- **Register users**, with email checking and duplicate-email detection
- **Assign courses.** Switching course resets a student's progress.
- **Submit assignments.** A student must be enrolled first, and submitting the same assignment twice is refused. Progress is tracked as a percentage.
- **Assign mentors.** Each mentor can take up to 3 students, and a student can be moved from one mentor to another.
- **Display student information:** course, mentor, assignments and progress
- **Display mentor information:** expertise, number of students and each student's progress
- **Count users:** total users, students and mentors
- **Rename the platform** for every user with a class method

## OOP Concepts Covered

| Concept | Implementation |
|---|---|
| **Classes and inheritance** | `Student(User)` and `Mentor(User)` |
| **Constructors** | `User.__init__` checks the email and counts the user. The child classes call it through `super()`. |
| **Class variables** | `platform_name`, `total_users`, `total_students`, `total_mentors`, `MAX_STUDENTS` |
| **Class methods** | `User.get_total_users()`, `User.rename_platform()` |
| **Static method** | `User.is_valid_email(email)` |
| **Instance methods** | `assign_course()`, `submit_assignment()`, `progress()`, `assign_student()`, `display_info()` |
| **Method overriding** | `display_info()` and `role()` in each child class |
| **Multiple objects** | 4 students + 2 mentors |

## Project Structure

```
.
├── super30_platform.py   # User, Student, Mentor classes + demo
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

```bash
# Mac / Linux
python3 super30_platform.py

# Windows
python super30_platform.py
```

## Usage Example

```python
from super30_platform import User, Student, Mentor

print(User.is_valid_email("aarav@super30.in"))   # True

s1 = Student("Aarav Sharma", "aarav@super30.in", "STU101")
m1 = Mentor("Dr. Anita Rao", "anita@super30.in", "MEN201", "Data Structures & Algorithms")

s1.assign_course("DSA Mastery")
m1.assign_student(s1)
s1.submit_assignment("Arrays & Hashing")    # 10% complete

s1.display_info()
m1.display_info()
print(User.get_total_users())               # 2
```

## Sample Output

```
============ 2. Registering users (constructors + objects) ============
Registered 6 users.
Registration rejected: Invalid email address: 'fake-email'
Registration rejected: Email already registered: 'aarav@super30.in'

============ 4. Assigning mentors ============
Cannot assign Rohan Mehta: Dr. Anita Rao is at full capacity (3 students).
Rohan Mehta assigned to mentor Vikram Nair (Machine Learning).
Neha Gupta assigned to mentor Vikram Nair (Machine Learning).

============ 5. Submitting assignments ============
Aarav Sharma submitted 'Sliding Window' (30% of DSA Mastery complete).
Submission rejected: Aarav Sharma already submitted 'Two Pointers'.

============ 9. Platform statistics ============
Total users    : 6
  Students     : 4
  Mentors      : 2
Top performer  : Aarav Sharma (3 assignments)
```

## Method Reference

| Method | Class | Type | Description |
|---|---|---|---|
| `__init__(name, email, user_id)` | User | Constructor | Checks the email, rejects duplicates, adds 1 to `total_users` |
| `is_valid_email(email)` | User | Static | Checks the basic email format |
| `get_total_users()` | User | Class | Returns the total number of registered users |
| `rename_platform(new_name)` | User | Class | Changes the platform name for every user |
| `display_info()` | User | Instance | Prints the platform, role, ID, name and email |
| `assign_course(course_name)` | Student | Instance | Enrolls the student in a course, or switches course and resets progress |
| `submit_assignment(name)` | Student | Instance | Records an assignment. Refuses duplicates and students with no course. |
| `progress()` | Student | Instance | Returns the percentage of the 10 course assignments completed |
| `display_info()` | Student | Override | Adds course, mentor and assignment details |
| `assign_student(student)` | Mentor | Instance | Assigns a student within the 3-student limit and moves them from any previous mentor |
| `display_info()` | Mentor | Override | Adds expertise and each assigned student's progress |

## Possible Enhancements

- Mentors grade assignments and give feedback
- Save users and progress to a JSON or CSV file
- An interactive menu for registering users and submitting work
- An `Admin` child class that manages courses
