"""
Online Learning Platform - Inheritance Demo
Demonstrates: parent class, child class, inheritance, super(),
method overriding, class variables, and class methods.

    Course            (parent: standard self-paced course)
       |
    PremiumCourse     (child: adds mentor support + live sessions)
"""


# ================= Parent Class =================
class Course:
    # Class variable: counts EVERY course created (standard + premium)
    course_count = 0

    def __init__(self, course_name, instructor, duration_weeks, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.course_name = course_name
        self.instructor = instructor
        self.duration_weeks = duration_weeks
        self.price = price

        Course.course_count += 1

    def show_course_details(self):
        """Print the details every course shares."""
        print(f"Course      : {self.course_name}")
        print(f"Type        : {self.course_type()}")
        print(f"Instructor  : {self.instructor}")
        print(f"Duration    : {self.duration_weeks} weeks")
        print(f"Price       : ${self.price:,.2f}")

    def course_type(self):
        return "Standard (self-paced)"

    def calculate_discount(self, percent):
        """Return the price after a percentage discount (0-100)."""
        if not 0 <= percent <= 100:
            print(f"Invalid discount {percent}%. Using 0%.")
            percent = 0
        discounted = self.price - (self.price * percent / 100)
        return round(discounted, 2)

    # ---------- Class method ----------
    @classmethod
    def get_course_count(cls):
        """Return the total number of courses created on the platform."""
        return Course.course_count


# ================= Child Class =================
class PremiumCourse(Course):
    # Platform rule: premium courses include paid mentor time,
    # so discounts on them are capped.
    MAX_DISCOUNT = 30

    def __init__(self, course_name, instructor, duration_weeks, price,
                 mentor_support, live_sessions):
        # Reuse the parent constructor (this also increments course_count)
        super().__init__(course_name, instructor, duration_weeks, price)
        self.mentor_support = mentor_support    # True / False
        self.live_sessions = live_sessions      # number of live classes

    def course_type(self):
        return "Premium (mentor-led)"

    def show_course_details(self):
        """Override: print the parent details, then the premium extras."""
        super().show_course_details()
        print(f"Mentor      : {'1:1 mentor support' if self.mentor_support else 'Not included'}")
        print(f"Live classes: {self.live_sessions} sessions")

    def calculate_discount(self, percent):
        """Override: cap the discount, then reuse the parent calculation."""
        if percent > PremiumCourse.MAX_DISCOUNT:
            print(f"Note: premium discounts are capped at {PremiumCourse.MAX_DISCOUNT}% "
                  f"(requested {percent}%).")
            percent = PremiumCourse.MAX_DISCOUNT
        return super().calculate_discount(percent)


# ================= Demo =================
if __name__ == "__main__":
    catalog = [
        Course("Python for Beginners", "Anita Rao", 6, 49.00),
        Course("SQL Fundamentals", "Vikram Nair", 4, 39.00),
        PremiumCourse("Data Science Bootcamp", "Dr. Meera Iyer", 16, 499.00,
                      mentor_support=True, live_sessions=24),
        PremiumCourse("Machine Learning Mastery", "Arjun Kapoor", 12, 399.00,
                      mentor_support=True, live_sessions=12),
        PremiumCourse("Power BI Dashboards", "Sana Sheikh", 5, 149.00,
                      mentor_support=False, live_sessions=4),
    ]

    print("=== Course Catalog ===")
    for course in catalog:
        print("-" * 44)
        course.show_course_details()   # right version picked automatically
    print("-" * 44)

    print("\n=== Festive Sale: 40% off everything ===")
    for course in catalog:
        final = course.calculate_discount(40)
        print(f"{course.course_name:<26} ${course.price:>7,.2f} -> ${final:>7,.2f}")

    print("\n=== Inheritance in action ===")
    ds = catalog[2]
    print(f"Premium course reads parent attributes: "
          f"{ds.instructor}, {ds.duration_weeks} weeks")
    print(f"Premium 10% discount (within cap)     : ${ds.calculate_discount(10):,.2f}")
    print(f"isinstance(ds, Course)                : {isinstance(ds, Course)}")
    print(f"issubclass(PremiumCourse, Course)     : {issubclass(PremiumCourse, Course)}")
    print(f"Standard course has live_sessions?    : {hasattr(catalog[0], 'live_sessions')}")

    print("\n=== Platform Stats (class method) ===")
    premium = sum(isinstance(c, PremiumCourse) for c in catalog)
    print(f"Total courses created : {Course.get_course_count()}")
    print(f"  Standard            : {Course.get_course_count() - premium}")
    print(f"  Premium             : {premium}")