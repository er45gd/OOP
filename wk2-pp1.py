#operation identifier
print ("Which operation do you want to do?:")
print ("1=addition, 2=subtraction, 3=multiplication, and 4=division")
y=int(input())

#get values
print ("please enter the first value:")
a = int(input())
print ("please enter the second value:")
b = int(input())

#addition
if (y==1):
    c = a + b
    print("the sum of the two values is:", c)
#Subtraction
elif (y==2):
    c = a - b
    print("the difference of the two values is:", c)
#Multiplication
elif (y==3):
    c = a * b
    print("the product of the two values is:", c)
#Division
elif (y==4):
    print ("which division do you want?")
    print ("1=normal, 2=decimal, 3=rounding")
    divisionType = int(input())

    if (b==0):
        print("no no no, you cant divide by zero you code breaker")
        exit()

    if (divisionType == 1):
        c = a / b
        print("the dividend of the two values is:", c)
    elif (divisionType == 2):
        c = a % b
        print("the dividend of the two values is:", c)
    elif (divisionType == 3):
        c = a // b
        print("the dividend of the two values is:", c)

#user error
else:
    print("ERROR, wrong input, no operation found")