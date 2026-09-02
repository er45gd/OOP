while (True):
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    choice = (input("Enter your choice:"))

    print("input first number")
    a = int(input())
    print("input second number")
    b = int(input())

    if choice == "1":
        c=a+b
        print(c)

    elif choice == "2":
        c=a-b
        print(c)

    elif choice == "3":
        c=a*b
        print(c)

    elif choice == "4":
        if(b==0):
            print("your trying to divide by zero")
            exit()
        c=a/b
        print(c)
    else:
        print("invalid option")

    print("do you want to continue?:")
    exitCondition= input()
    if exitCondition == "no":
        exit()
    else:
        continue