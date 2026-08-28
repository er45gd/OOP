number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
#print(number1)
#print(number2)
print("")

if number1 > number2:
    print("number1 is the biggest")
elif number1== number2:
    print("they are equal")
elif number1 < number2:
    print("number2 is the biggest")
# code below is useless or mess up code below it if moved up
#elif number1 != number2:
#   print("they are not equal")
else:
    print("invalid numbers")