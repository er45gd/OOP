while True:
    print("which operation do you want to do:")
    print("1. area of a rectangle")
    print("2. volume of a cube")
    print("3. area of a circle")
    print("4. circumference of a circle")
    userChoice=input("enter your choice as a number: ")

    #area rectangle
    if userChoice == "1":
        height=float(input("what is the height"))
        length=float(input("what is the length"))
        area=height*length
        print("the area of the rectangle is ",area)
    #volume rectangular prism
    elif userChoice == "2":
        height=float(input("what is the height"))
        length=float(input("what is the length"))
        width=float(input("what is the width"))
        volume=height*length*width
        print("the volume of the rectangle is ",volume)
    #area circle
    elif userChoice == "3":
        radius = float(input("what is the radius"))
        radiusSquare= radius * radius
        area= radiusSquare*3.14
        print("the area of the circle is ",area)
    #circumference
    elif userChoice == "4":
        radius = float(input("what is the radius"))
        circumference=2*3.14*radius
        print("the circumference of the circle is ",circumference)

    else:
        print("enter a valid choice")

    print("")
    print("do you want to continue operations")
    leave=str(input())
    if leave == "no":
        exit()
    elif leave == "yes":
        continue
    else:
        print("enter a valid choice, continuing operation")