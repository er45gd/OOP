def add():
    a=int(input("Enter a number"))
    b=int(input("Enter another number"))
    c=a+b
    print(c)
def sub():
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    c = a - b
    print(c)
def mul():
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
    c = a * b
    print(c)
def div():
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
    c = a / b
    print(c)

choose=int(input("Enter a choice"))
if choose==1:
    add()
elif choose==2:
    sub()
elif choose==3:
    mul()
elif choose==4:
    div()