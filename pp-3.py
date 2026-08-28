#find biggest
#find smallest
number1= int(input("enter first number: "))
number2= int(input("enter second number: "))
number3= int(input("enter third number: "))
print ("")

#code that ended up useless
#if number1 > number2:
#   greatOne= number1
#else:
#   greatTwo= number2

#bigger
if number3 >  number1:
    if number3 > number2:
        print("number3 is the greatest value")
    else:
        print("number2 is the greatest value")

if number3 < number1:
    if number2 < number1:
        print("number1 is the greatest value")
    else:
        print("number2 is the greatest value")
else
#smaller
if number3 <  number1:
    if number3 < number2:
        print("number3 is the smallest value")
    else:
        print("number2 is the smallest value")

if number3 > number1:
    if number2 > number1:
        print("number1 is the smallest value")
    else:
        print("number2 is the smallest value")

if number3 < number1 and number3 < number2:
    print ("number3 is the smallest value")
elif number2 < number1 and number2 < number3:
    print("number2 is the smallest value")
elif number1 < number2 and number1 < number3:
    print("number1 is the smallest value")
