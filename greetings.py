class Student:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.student_id = None
        self.classroom = None

    def welcome(self):
        return f"Welcome to Albert School, {self.first_name}!"

    def register(self, registry):
        self.student_id = len(registry) + 1
        registry.append(self)
        return self.student_id

    def enroll(self, classroom):
        self.classroom = classroom
        return f"{self.first_name} {self.last_name} joins {classroom}."


if __name__ == "__main__":
    registry = []
    student = Student("Tuka", "Bade", "tuka@albertschool.com")
    student.register(registry)
    print(student.welcome())
    print(f"Registered as student #{student.student_id}")
    print(f"Confirmation sent to {student.email}")
    print(student.enroll("MSc 1 Data"))