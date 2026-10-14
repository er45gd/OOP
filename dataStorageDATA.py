import pickle

class Student:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.department = ""

    def create_student(self):
        self.name = input("Enter name: ")
        self.id = input("Enter student ID: ")
        self.department = input("Enter department: ")
        print()

    def display_student(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.department)
        print()

#main
s1 = Student()
s1.create_student()
s1.display_student()

file1=open("likeandsubscribe.dat", "ab")
pickle.dump(s1, file1)
file1.close()

file2=open("likeandsubscribe.dat", "rb")

while(1):
    try:
        data =pickle.load(file2)
        print(data.name)
        print(data.id)
        print(data.department)

    except (EOFError):
        break
file2.close()