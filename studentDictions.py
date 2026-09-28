students= {}

while True:
    i=1
    print ("choose operation")
    print("enter '1' to add a student")
    print("enter '2' to remove a student")
    print("enter '3' to edit a student")
    print("enter '4' to view all students")
    print("enter '5' to exit")
    choice=int(input())
    if choice==1:
        name=input("Enter student name: ")
        major=input("Enter major: ")
        year=input("Enter year: ")

        students.update({"s"+str(i):
                                     {
                                        "stu_name": name,
                                        "stu_major": major,
                                        "stu_year": year
                                     }
                        }
                     )



    elif choice==2:
        name=input("Enter student's number to remove: ")
        answer="s"+name
        students.pop(answer)

    elif choice==3:
        choice=input("Enter student's number to edit: ")
        name=input("Enter student name: ")
        major=input("Enter major: ")
        year=input("Enter year: ")
        students.update({"s"+str(choice):
                                    {
                                    "stu_name": name,
                                    "stu_major": major,
                                    "stu_year": year
                                     }
                                }
                        )

    elif choice==4:
        print(students)

    elif choice==5:
        exit()

    else:
        print("Enter a valid choice")