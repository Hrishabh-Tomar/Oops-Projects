# Task 3: Employee & Developer Inheritance (Python OOP)

A demonstration of **single inheritance** in Python. A `Developer` class inherits from an `Employee` base class. It reuses the parent's attributes and methods and adds developer-specific details of its own.

```
Employee        (parent / base class)
   |
Developer       (child / derived class)
```

## Features

- Create general employees and developers
- Display details. A developer's output shows the employee fields plus language and experience.
- Give a salary raise with a method that lives only in the parent class
- A developer-only method, `write_code()`
- Built-in checks (`isinstance`, `issubclass`) that confirm how the two classes are related

## OOP Concepts Covered

| Concept | Implementation |
|---|---|
| **Parent class** | `Employee` stores `emp_id`, `name`, `salary`, `department` |
| **Child class** | `Developer(Employee)` adds `programming_language` and `experience` |
| **Inheritance** | `Developer` gets `give_raise()` and every parent attribute without redefining them |
| **`super()`** | `Developer.__init__` reuses the parent constructor, and `display_details()` extends the parent's version |
| **Method overriding** | `Developer.display_details()` |
| **Object creation** | 1 `Employee` + 2 `Developer` objects |

## Project Structure

```
.
├── employee_inheritance.py   # Employee + Developer classes + demo
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

```bash
# Mac / Linux
python3 employee_inheritance.py

# Windows
python employee_inheritance.py
```

## Usage Example

```python
from employee_inheritance import Employee, Developer

dev = Developer("D201", "Aarav Sharma", 95000, "Engineering", "Python", 4)

print(dev.name)          # attribute set up by the parent class
dev.give_raise(10)       # method written only in the parent class
dev.display_details()    # parent's details + developer fields
dev.write_code()         # method only developers have
```

## Sample Output

```
=== 3. Child calling a parent method it never defined ===
Aarav Sharma: salary raised 10% ($95,000.00 -> $104,500.00)

=== 4. Child-only method ===
Priya Verma is writing code in Java.
Does Employee have write_code()? False

=== 5. Checking the relationship ===
issubclass(Developer, Employee) -> True
isinstance(dev1, Employee)      -> True
isinstance(emp1, Developer)     -> False
```

## Method Reference

| Method | Class | Description |
|---|---|---|
| `__init__(emp_id, name, salary, department)` | Employee | Sets the common employee attributes |
| `display_details()` | Employee | Prints ID, name, department and salary |
| `give_raise(percent)` | Employee | Raises salary by a percentage. Developers inherit it. |
| `__init__(..., programming_language, experience)` | Developer | Calls `super().__init__()`, then adds the developer fields |
| `display_details()` | Developer | Override: prints the parent's details, then language and experience |
| `write_code()` | Developer | Developer-only method |

## Possible Enhancements

- Add more child classes, such as `Manager` or `Designer`
- Calculate a bonus differently for each role
- Track the team a developer belongs to
