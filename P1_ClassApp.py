class Student:
    def __init__(self, name):
        # initialize student's detail 
        self.name = name
        self.attendance = 0
        self.grades = {}
    
    # Mark attendance
    def mark_attendance(self):
        self.attendance += 1
        print(f"{self.name}'s attendance marked.")
    
    # Add grade for subject
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Grade {grade} added for {self.name} in {subject}.")
    
    # Show student details 
    def show_info(self):
        print(f"Name: {self.name}, Attendance: {self.attendance}, Grades: {self.grades}")


class Classroom:
    def __init__(self):
        # initialize classroom with empty dict
        self.students = {}
    
    # Add new student
    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"{name} added to class.")
        else:
            print("Student already exists.")
    
    # Remove student
    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"{name} removed.")
        else:
            print("Student not found.")
    
    # Mark attendance
    def mark_attendance(self, name):
        if name in self.students:
            self.students[name].mark_attendance()
        else:
            print("Student not found.")
    
    # Add grade
    def add_grade(self, name, subject, grade):
        if name in self.students:
            self.students[name].add_grade(subject, grade)
        else:
            print("Student not found.")
    
    # Show all students 
    def show_student(self):
        if self.students:
            for student in self.students.values():
                student.show_info()
        else:
            print("No students enrolled.")


# Main program menu
def main():
    classroom = Classroom()
    while True:
        print("\n1. Add student\n2. Remove student\n3. Mark attendance\n4. Add grade\n5. Show students\n6. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            classroom.add_student(input("Enter name: "))
        elif choice == "2":
            classroom.remove_student(input("Enter name: "))
        elif choice == "3":
            classroom.mark_attendance(input("Enter name: "))
        elif choice == "4":
            classroom.add_grade(input("Enter name: "), input("Enter subject: "), input("Enter grade: "))
        elif choice == "5":
            classroom.show_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
