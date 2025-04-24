class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.attendance = []

    def mark_attendance(self, date):
        self.attendance.append(date)

    def __repr__(self):
        return f'Student(ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Attendance: {len(self.attendance)} days)'

    
class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def __repr__(self):
        return f'Teacher(ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject})'


class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, student_id, name, age):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name, age)
            print(f'Student {name} added successfully.')
        else:
            print('Student ID already exists.')

    def add_teacher(self, teacher_id, name, subject):
        if teacher_id not in self.teachers:
            self.teachers[teacher_id] = Teacher(teacher_id, name, subject)
            print(f'Teacher {name} added successfully.')
        else:
            print('Teacher ID already exists.')

    def mark_attendance(self, student_id, date):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date)
            print(f'Attendance marked for {self.students[student_id].name} on {date}.')
        else:
            print('Student ID not found.')

    def view_students(self):
        for student in self.students.values():
            print(student)

    def view_teachers(self):
        for teacher in self.teachers.values():
            print(teacher)


def main():
    sms = SchoolManagementSystem()

    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Mark Attendance")
        print("4. View Students")
        print("5. View Teachers")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            sms.add_student(student_id, name, age)

        elif choice == '2':
            teacher_id = input("Enter Teacher ID: ")
            name = input("Enter Teacher Name: ")
            subject = input("Enter Teacher Subject: ")
            sms.add_teacher(teacher_id, name, subject)

        elif choice == '3':
            student_id = input("Enter Student ID for Attendance: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            sms.mark_attendance(student_id, date)

        elif choice == '4':
            sms.view_students()

        elif choice == '5':
            sms.view_teachers()

        elif choice == '6':
            print("Exiting the School Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
