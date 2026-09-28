"""
Super30 Learning Platform - OOP Capstone
Covers: class, objects, constructors (__init__), instance methods,
class variables, class methods, static methods, inheritance,
super(), and method overriding.

    User
     |
     +---- Student   (course, completed assignments)
     |
     +---- Mentor    (expertise, assigned students)
"""


# ======================= Parent Class =======================
class User:
    # ---- Class variables (shared by all users) ----
    platform_name = "Super30 Learning Platform"
    total_users = 0
    _registered_emails = set()      # prevents duplicate registrations

    def __init__(self, name, email, user_id):
        # Static method used inside the constructor for validation
        if not User.is_valid_email(email):
            raise ValueError(f"Invalid email address: '{email}'")
        if email.lower() in User._registered_emails:
            raise ValueError(f"Email already registered: '{email}'")

        self.name = name
        self.email = email
        self.user_id = user_id

        User._registered_emails.add(email.lower())
        User.total_users += 1

    # ---- Static method: utility that needs no object or class data ----
    @staticmethod
    def is_valid_email(email):
        """Basic check: exactly one '@' and a '.' in the domain part."""
        if not isinstance(email, str) or email.count("@") != 1:
            return False
        local, domain = email.split("@")
        return bool(local) and "." in domain and not domain.startswith(".") \
            and not domain.endswith(".")

    # ---- Class methods: work on class-level data ----
    @classmethod
    def get_total_users(cls):
        return User.total_users

    @classmethod
    def rename_platform(cls, new_name):
        print(f"Platform renamed: '{User.platform_name}' -> '{new_name}'")
        User.platform_name = new_name

    # ---- Instance methods ----
    def role(self):
        return "User"

    def display_info(self):
        print(f"Platform     : {User.platform_name}")
        print(f"Role         : {self.role()}")
        print(f"User ID      : {self.user_id}")
        print(f"Name         : {self.name}")
        print(f"Email        : {self.email}")


# ======================= Child Class 1 =======================
class Student(User):
    total_students = 0
    TOTAL_ASSIGNMENTS_PER_COURSE = 10

    def __init__(self, name, email, user_id, course_name=None):
        super().__init__(name, email, user_id)
        self.course_name = course_name
        self.completed_assignments = []
        self.mentor = None
        Student.total_students += 1

    def role(self):
        return "Student"

    def assign_course(self, course_name):
        """Enroll in a course. Switching courses resets progress."""
        if self.course_name and self.course_name != course_name:
            print(f"{self.name}: switching from '{self.course_name}' to "
                  f"'{course_name}' (progress reset).")
            self.completed_assignments = []
        else:
            print(f"{self.name} enrolled in '{course_name}'.")
        self.course_name = course_name

    def submit_assignment(self, assignment_name):
        """Submit an assignment. Needs a course, and no duplicate submissions."""
        if not self.course_name:
            print(f"Submission rejected: {self.name} is not enrolled in any course.")
            return False
        if assignment_name in self.completed_assignments:
            print(f"Submission rejected: {self.name} already submitted '{assignment_name}'.")
            return False
        self.completed_assignments.append(assignment_name)
        print(f"{self.name} submitted '{assignment_name}' "
              f"({self.progress():.0f}% of {self.course_name} complete).")
        return True

    def progress(self):
        done = len(self.completed_assignments)
        return min(done / Student.TOTAL_ASSIGNMENTS_PER_COURSE * 100, 100)

    def display_info(self):
        super().display_info()
        print(f"Course       : {self.course_name or 'Not enrolled'}")
        print(f"Mentor       : {self.mentor.name if self.mentor else 'Not assigned'}")
        print(f"Assignments  : {len(self.completed_assignments)} completed "
              f"({self.progress():.0f}%)")
        if self.completed_assignments:
            print(f"               {', '.join(self.completed_assignments)}")


# ======================= Child Class 2 =======================
class Mentor(User):
    total_mentors = 0
    MAX_STUDENTS = 3

    def __init__(self, name, email, user_id, expertise):
        super().__init__(name, email, user_id)
        self.expertise = expertise
        self.students = []
        Mentor.total_mentors += 1

    def role(self):
        return "Mentor"

    @property
    def num_students(self):
        return len(self.students)

    def assign_student(self, student):
        """Assign a student to this mentor, respecting capacity."""
        if student in self.students:
            print(f"{student.name} is already assigned to {self.name}.")
            return False
        if self.num_students >= Mentor.MAX_STUDENTS:
            print(f"Cannot assign {student.name}: {self.name} is at full "
                  f"capacity ({Mentor.MAX_STUDENTS} students).")
            return False
        if student.mentor:                  # move from previous mentor
            student.mentor.students.remove(student)
        self.students.append(student)
        student.mentor = self
        print(f"{student.name} assigned to mentor {self.name} ({self.expertise}).")
        return True

    def display_info(self):
        super().display_info()
        print(f"Expertise    : {self.expertise}")
        print(f"Students     : {self.num_students}/{Mentor.MAX_STUDENTS}")
        for s in self.students:
            print(f"   - {s.name:<14} {s.course_name or 'No course':<30}"
                  f"{s.progress():.0f}% done")


# ======================= Demo =======================
def section(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


if __name__ == "__main__":
    section("1. Static method: email validation")
    for e in ("aarav@super30.in", "bad-email", "a@b", "priya@@mail.com"):
        print(f"User.is_valid_email('{e}') -> {User.is_valid_email(e)}")

    section("2. Registering users (constructors + objects)")
    s1 = Student("Aarav Sharma", "aarav@super30.in", "STU101")
    s2 = Student("Priya Verma", "priya@super30.in", "STU102")
    s3 = Student("Rohan Mehta", "rohan@super30.in", "STU103")
    s4 = Student("Neha Gupta", "neha@super30.in", "STU104")
    m1 = Mentor("Dr. Anita Rao", "anita@super30.in", "MEN201", "Data Structures & Algorithms")
    m2 = Mentor("Vikram Nair", "vikram@super30.in", "MEN202", "Machine Learning")
    print(f"Registered {User.get_total_users()} users.")

    for bad in (("Fake User", "fake-email", "STU999"),
                ("Aarav Copy", "aarav@super30.in", "STU998")):
        try:
            Student(*bad)
        except ValueError as err:
            print(f"Registration rejected: {err}")

    section("3. Assigning courses")
    s1.assign_course("DSA Mastery")
    s2.assign_course("DSA Mastery")
    s3.assign_course("Machine Learning Foundations")
    s4.assign_course("DSA Mastery")
    s4.assign_course("Machine Learning Foundations")   # switch course

    section("4. Assigning mentors")
    m1.assign_student(s1)
    m1.assign_student(s2)
    m1.assign_student(s4)
    m1.assign_student(s3)          # capacity full -> rejected
    m2.assign_student(s3)
    m2.assign_student(s4)          # moves Neha from m1 to m2

    section("5. Submitting assignments")
    s1.submit_assignment("Arrays & Hashing")
    s1.submit_assignment("Two Pointers")
    s1.submit_assignment("Sliding Window")
    s1.submit_assignment("Two Pointers")           # duplicate -> rejected
    s2.submit_assignment("Arrays & Hashing")
    s3.submit_assignment("Linear Regression")
    s3.submit_assignment("Logistic Regression")
    s4.submit_assignment("Linear Regression")

    section("6. Student information")
    for s in (s1, s2, s3, s4):
        print("-" * 50)
        s.display_info()
    print("-" * 50)

    section("7. Mentor information")
    for m in (m1, m2):
        print("-" * 50)
        m.display_info()
    print("-" * 50)

    section("8. Class method: rename platform for everyone")
    User.rename_platform("Super30 Academy")
    print(f"s1 sees: {s1.platform_name} | m2 sees: {m2.platform_name}")

    section("9. Platform statistics")
    print(f"Total users    : {User.get_total_users()}")
    print(f"  Students     : {Student.total_students}")
    print(f"  Mentors      : {Mentor.total_mentors}")
    top = max((s1, s2, s3, s4), key=lambda s: len(s.completed_assignments))
    print(f"Top performer  : {top.name} ({len(top.completed_assignments)} assignments)")

    section("10. Inheritance checks")
    print(f"isinstance(s1, User)       -> {isinstance(s1, User)}")
    print(f"isinstance(m1, Student)    -> {isinstance(m1, Student)}")
    print(f"issubclass(Mentor, User)   -> {issubclass(Mentor, User)}")