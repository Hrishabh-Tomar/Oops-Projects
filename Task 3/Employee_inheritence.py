"""
Employee Management - Inheritance Demo
Demonstrates: parent class, child class, inheritance,
super(), method overriding, and object creation.

    Employee        (parent / base class)
       |
    Developer       (child / derived class)
"""


# ================= Parent Class =================
class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        """Print the common employee details."""
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : ${self.salary:,.2f}")

    def give_raise(self, percent):
        """Parent method that every child class inherits."""
        old_salary = self.salary
        self.salary += self.salary * percent / 100
        print(f"{self.name}: salary raised {percent}% "
              f"(${old_salary:,.2f} -> ${self.salary:,.2f})")


# ================= Child Class =================
class Developer(Employee):
    def __init__(self, emp_id, name, salary, department,
                 programming_language, experience):
        # Reuse the parent constructor for the shared attributes
        super().__init__(emp_id, name, salary, department)
        # Attributes unique to Developer
        self.programming_language = programming_language
        self.experience = experience  # in years

    def display_details(self):
        """Override: reuse the parent's output, then add developer fields."""
        super().display_details()
        print(f"Language    : {self.programming_language}")
        print(f"Experience  : {self.experience} years")

    def write_code(self):
        """Method that only Developer objects have."""
        print(f"{self.name} is writing code in {self.programming_language}.")


# ================= Demo =================
if __name__ == "__main__":
    # Object creation: 1 Employee + 2 Developers
    emp1 = Employee("E101", "Neha Gupta", 65000, "Human Resources")
    dev1 = Developer("D201", "Aarav Sharma", 95000, "Engineering", "Python", 4)
    dev2 = Developer("D202", "Priya Verma", 110000, "Engineering", "Java", 7)

    staff = [emp1, dev1, dev2]

    print("=== 1. Display details (same method name, different classes) ===")
    for person in staff:
        print("-" * 36)
        print(f"[{type(person).__name__}]")
        person.display_details()
    print("-" * 36)

    print("\n=== 2. Child accessing parent attributes directly ===")
    print(f"dev1.name       -> {dev1.name}        (defined in Employee)")
    print(f"dev1.department -> {dev1.department}   (defined in Employee)")
    print(f"dev1.programming_language -> {dev1.programming_language} (defined in Developer)")

    print("\n=== 3. Child calling a parent method it never defined ===")
    dev1.give_raise(10)   # give_raise() lives only in Employee
    emp1.give_raise(5)

    print("\n=== 4. Child-only method ===")
    dev2.write_code()
    print(f"Does Employee have write_code()? {hasattr(emp1, 'write_code')}")

    print("\n=== 5. Checking the relationship ===")
    print(f"issubclass(Developer, Employee) -> {issubclass(Developer, Employee)}")
    print(f"isinstance(dev1, Employee)      -> {isinstance(dev1, Employee)}")
    print(f"isinstance(emp1, Developer)     -> {isinstance(emp1, Developer)}")