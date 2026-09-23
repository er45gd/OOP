myStack=['1','2','3','4','5']

def push():
    print("what to add")
    item=input()
    myStack.append(item)
def pop():
    print("removing last value")
    myStack.pop()


while True:
    print(myStack)
    print("1=push, 2=pop, 3=exit")
    x=int(input())
    if x==1:
        push()
    elif x==2:
        pop()
    elif x==3:
        break
    else:
        print("enter a valid number")