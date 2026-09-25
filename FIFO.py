myQ=[]

def deq():
    del myQ[0]
    print("person first in line helped")

def enq():
    v=input("what do you want to add to the line?: ")
    myQ.append(v)

#main
while True:

    print("the current length of the line is: ", len(myQ))
    print("help the person or add another person")
    print("1 to help, 2 to add, exit to finish, or view to see.")
    ing=input()
    ing=ing.lower()
    if ing=="1":
        deq()

    elif ing=="2":
       enq()

    elif ing=="f":
        print("No one died, why did you do that?")

    elif ing=="exit":
        break
    elif ing=="view":
        print(myQ)
    else:
        print("please enter a valid option")

    print("")