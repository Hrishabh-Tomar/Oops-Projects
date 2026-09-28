"""
Student Management System
Demonstrates: class, objects, __init__, instance methods,
class variable, and class method.
"""


class Student:
    # Class variable: shared by every Student object
    total_students = 0

    def __init__(self, name, email, student_id, course, marks=None):
        # Instance variables: unique to each object
        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = marks if marks is not None else {}  # {subject: score}

        # Every new object increments the shared counter
        Student.total_students += 1

    # ---------- Instance methods ----------
    def display_details(self):
        """Print all details of this student."""
        print("-" * 40)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Course     : {self.course}")
        if self.marks:
            print("Marks      :")
            for subject, score in self.marks.items():
                print(f"   {subject:<12}: {score}")
        else:
            print("Marks      : No marks recorded")
        print(f"Average    : {self.calculate_average():.2f}")
        print("-" * 40)

    def update_marks(self, subject, new_score):
        """Add or update the score for a subject (0–100)."""
        if not 0 <= new_score <= 100:
            print(f"Invalid score {new_score}. Marks must be between 0 and 100.")
            return
        old_score = self.marks.get(subject)
        self.marks[subject] = new_score
        if old_score is None:
            print(f"Added {subject}: {new_score} for {self.name}")
        else:
            print(f"Updated {subject} for {self.name}: {old_score} -> {new_score}")

    def calculate_average(self):
        """Return the average of all marks, or 0 if none exist."""
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    # ---------- Class method ----------
    @classmethod
    def get_total_students(cls):
        """Return the total number of Student objects created."""
        return cls.total_students

    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.course}"


# ---------------- Demo ----------------
if __name__ == "__main__":
    # Creating multiple student objects
    s1 = Student("Aarav Sharma", "aarav@example.com", "S101", "Data Science",
                 {"Python": 88, "Statistics": 76, "SQL": 91})
    s2 = Student("Priya Verma", "priya@example.com", "S102", "Business Analytics",
                 {"Python": 72, "Excel": 85, "Statistics": 80})
    s3 = Student("Rohan Mehta", "rohan@example.com", "S103", "Computer Science")

    print("\n=== All Students ===")
    for student in (s1, s2, s3):
        student.display_details()

    print("\n=== Updating Marks ===")
    s1.update_marks("Statistics", 84)   # update existing subject
    s3.update_marks("Python", 90)       # add new subject
    s3.update_marks("Java", 78)
    s2.update_marks("Excel", 105)       # invalid score, rejected

    print("\n=== Averages After Update ===")
    for student in (s1, s2, s3):
        print(f"{student.name:<15} -> {student.calculate_average():.2f}")

    print("\n=== Class Method ===")
    print(f"Total students: {Student.get_total_students()}")