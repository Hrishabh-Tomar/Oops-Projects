# Python OOP Assignments (Tasks 1–7)

Seven Python programs that build Object-Oriented Programming skills step by step, starting with a single class and ending with a full learning-platform capstone. Every program is self-contained, needs no external libraries and includes a demo that runs when you execute the file.

## Tasks at a Glance

| # | Task | File | Key Concepts |
|---|---|---|---|
| 1 | Student Management System | `student_management.py` | Class, objects, `__init__`, instance methods, class variable, class method |
| 2 | Simplified Banking Application | `bank_account.py` | Class variables, class methods, input validation |
| 3 | Employee & Developer | `employee_inheritance.py` | Parent/child class, single inheritance, `super()`, overriding |
| 4 | E-Commerce Product Store | `product_store.py` | Static method, instance methods, stock validation |
| 5 | Online Learning Platform | `learning_platform.py` | Inheritance, overriding, class variable + class method |
| 6 | Vehicle Rental Application | `vehicle_rental.py` | Hierarchical inheritance, static method |
| 7 | **Super30 Learning Platform (Capstone)** | `super30_platform.py` | All of the above combined |

## Concept Coverage

| Concept | T1 | T2 | T3 | T4 | T5 | T6 | T7 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Class & objects | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Constructor (`__init__`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Instance methods | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Class variable | ✅ | ✅ |  |  | ✅ |  | ✅ |
| Class method | ✅ | ✅ |  |  | ✅ |  | ✅ |
| Static method |  |  |  | ✅ |  | ✅ | ✅ |
| Inheritance & `super()` |  |  | ✅ |  | ✅ | ✅ | ✅ |
| Method overriding |  |  | ✅ |  | ✅ | ✅ | ✅ |
| Input validation | ✅ | ✅ |  | ✅ | ✅ | ✅ | ✅ |

## Project Structure

```
.
├── student_management.py     # Task 1
├── bank_account.py           # Task 2
├── employee_inheritance.py   # Task 3
├── product_store.py          # Task 4
├── learning_platform.py      # Task 5
├── vehicle_rental.py         # Task 6
├── super30_platform.py       # Task 7 (capstone)
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

Open a terminal in the project folder and run any task:

```bash
# Mac / Linux
python3 student_management.py
python3 bank_account.py
python3 employee_inheritance.py
python3 product_store.py
python3 learning_platform.py
python3 vehicle_rental.py
python3 super30_platform.py

# Windows: use "python" instead of "python3"
python super30_platform.py
```

## Task Summaries

### Task 1: Student Management System
A `Student` class with name, email, ID, course and marks for each subject. Students' details can be displayed, marks can be updated (0–100 only) and averages calculated. A class variable counts the students and `get_total_students()` returns the count.

### Task 2: Simplified Banking Application
A `BankAccount` class with `deposit()`, `withdraw()`, `check_balance()` and `display_account_details()`. Withdrawals larger than the balance are refused. The class variable `bank_name` can be changed for every account with the class method `change_bank_name()`. **Bonus:** counts the total accounts created.

### Task 3: Employee & Developer (Inheritance)
`Developer` inherits from `Employee` and adds a programming language and years of experience. The demo shows a developer using parent attributes and the parent-only `give_raise()` method, and extending `display_details()` with `super()`.

### Task 4: E-Commerce Product Store
A `Product` class with `display_product()`, `update_stock()`, `calculate_total_price()` and `buy()`. The static method `Product.is_valid_price()` stops products from being created with a price of zero or less. The demo runs 5 products through purchases and restocks.

### Task 5: Online Learning Platform
`PremiumCourse` inherits from `Course` and adds mentor support and live sessions. It overrides `show_course_details()` and `calculate_discount()`, capping premium discounts at 30%. A class variable counts all courses and `get_course_count()` returns the count.

### Task 6: Vehicle Rental Application
`Car` and `Bike` both inherit from `Vehicle` (hierarchical inheritance). `calculate_rent(days)` is written once in the parent. The static method `Vehicle.is_valid_duration()` refuses rentals of zero or negative days. Vehicles can be rented and returned, and a rented vehicle can't be booked again until it comes back.

### Task 7: Super30 Learning Platform (Capstone)
`Student` and `Mentor` inherit from `User`. The platform covers registration with email checks, course enrollment, assignment submission with progress tracking, mentor assignment with a 3-student limit, profile displays and platform-wide user counts. It uses every concept from tasks 1–6.

## Individual READMEs

Each task also has its own detailed README:

- `README_task1_student_management.md`
- `README_task2_banking.md`
- `README_task3_employee_inheritance.md`
- `README_task4_product_store.md`
- `README_task5_learning_platform.md`
- `README_task6_vehicle_rental.md`
- `README_task7_super30_platform.md`
