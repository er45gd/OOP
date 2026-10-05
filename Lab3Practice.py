class Student:
    def __init__(self, name=""):

    def create_student(self):
        print("enter name: ")
        name = input()

    def enroll_student(self):
        print()




class Faculty:
    def create_faculty(self):
        print("enter name: ")
        name = input()
        print("enter new id code: ")


    def enroll_students(self):
        print()




class Courses:
    print()

#MAIN CODE
# faculty
print("how many faculty do you want to create")
x = int(input())

for i in range(x):
    fac = Faculty()
    fac.create_faculty
    fac.enroll_students(student_id)
    myFacultyList.append

    i = i + 1

#students
print("how many student do you want to create")
x=int(input())

for i in range(x):
    stu=Student()
    stu.create_student()
    stu.assign_advisor(faculty_id)
    myStudentList.append(fac)
    i=i+1

#idk it something
    faculty_id =(input("Enter Faculty ID: "))
    for x in myFucntionList:
        if x.fid == faculty_id:
            stu.assign_advisor(faculty_obj)

#courses
print("how many classes do you want to create")
x=int(input())

for i in range(x):
    cou =Courses()
    cou.create_course()
    cou.assign_faculty(faculty.id)
    cou.register_student(student.id)
    myCoursesList.append(cou)
    i=i+1