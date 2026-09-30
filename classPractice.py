class Students:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

    def assign_advisor(self):
        print("")

    def calculate_grade(self):
        print("")

class faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_staff(self):
        self.id = input("Enter faculty ID: ")
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def display_staff(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

    def class_schedule(selfself):
        print("")


#main program
myStudents = []

Stu = Students()
Stu.create_new_student()
Stu.display_student()

myStudents.append(Stu)

Stu = Students()
Stu.create_new_student()
Stu.display_student()

myStudents.append(Stu)
print(myStudents)