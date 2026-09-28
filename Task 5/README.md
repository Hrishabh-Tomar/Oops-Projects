# Task 5: Online Learning Platform (Python OOP)

Models an EdTech course catalog with inheritance. Standard self-paced courses are `Course` objects. Mentor-led courses are `PremiumCourse` objects, which inherit everything from `Course` and add premium features.

```
Course            (parent: standard self-paced course)
   |
PremiumCourse     (child: adds mentor support + live sessions)
```

## Features

- Create standard and premium courses
- Show course details. Premium courses also show mentor support and the number of live sessions.
- Calculate a discounted price
- Cap discounts on premium courses at 30%. This is an example business rule I added. To use the same discount for every course, remove `PremiumCourse.calculate_discount()`.
- Count every course created on the platform

## OOP Concepts Covered

| Concept | Implementation |
|---|---|
| **Parent class** | `Course` stores `course_name`, `instructor`, `duration_weeks`, `price` |
| **Child class** | `PremiumCourse(Course)` adds `mentor_support` and `live_sessions` |
| **Inheritance and `super()`** | The child constructor and methods reuse the parent's code |
| **Method overriding** | `show_course_details()`, `calculate_discount()`, `course_type()` |
| **Class variable** | `course_count` counts both standard and premium courses |
| **Class method** | `Course.get_course_count()` |
| **Objects** | 2 standard + 3 premium courses |

## Project Structure

```
.
├── learning_platform.py   # Course + PremiumCourse classes + demo
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

```bash
# Mac / Linux
python3 learning_platform.py

# Windows
python learning_platform.py
```

## Usage Example

```python
from learning_platform import Course, PremiumCourse

basic = Course("Python for Beginners", "Anita Rao", 6, 49.00)
pro = PremiumCourse("Data Science Bootcamp", "Dr. Meera Iyer", 16, 499.00,
                    mentor_support=True, live_sessions=24)

print(basic.calculate_discount(40))   # 29.4
print(pro.calculate_discount(40))     # 349.3 (capped at 30%)
pro.show_course_details()
print(Course.get_course_count())      # 2
```

## Sample Output

```
=== Festive Sale: 40% off everything ===
Python for Beginners       $  49.00 -> $  29.40
SQL Fundamentals           $  39.00 -> $  23.40
Note: premium discounts are capped at 30% (requested 40%).
Data Science Bootcamp      $ 499.00 -> $ 349.30

=== Platform Stats (class method) ===
Total courses created : 5
  Standard            : 2
  Premium             : 3
```

## Method Reference

| Method | Class | Description |
|---|---|---|
| `__init__(course_name, instructor, duration_weeks, price)` | Course | Creates a course and adds 1 to `course_count` |
| `show_course_details()` | Course | Prints the course details |
| `calculate_discount(percent)` | Course | Returns the price after a 0–100% discount |
| `get_course_count()` | Course (class method) | Returns the total number of courses created |
| `__init__(..., mentor_support, live_sessions)` | PremiumCourse | Calls `super().__init__()`, then adds the premium fields |
| `show_course_details()` | PremiumCourse | Override: prints the parent's details, then the premium extras |
| `calculate_discount(percent)` | PremiumCourse | Override: caps the discount at 30%, then uses the parent's calculation |

## Possible Enhancements

- Enroll students in courses and track how many are enrolled
- Add course ratings and reviews
- Add a `Bundle` class that combines several courses
