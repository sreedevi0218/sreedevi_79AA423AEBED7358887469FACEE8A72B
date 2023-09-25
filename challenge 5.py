def sort_students(students):
    students.sort(key=lambda student: student.cgpa, reverse=True)
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "A002", 3.5),
    Student("Charlie", "A003", 3.9),
]

# Sort the list of students based on CGPA
sort_students(students)

# Print the sorted list
for student in students:
    print(student.name, student.roll_number, student.cgpa)