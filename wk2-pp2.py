print("Name please:")
name = str(input())

print("input score for class one:")
classOne = int(input())
print("input score for class two:")
classTwo = int(input())
print("input score for class three:")
classThree =int(input())

total = classOne + classTwo + classThree    #MATH
gradePercentile= (total/300)*100
gradePercentile = gradePercentile//1    #formatting

if (gradePercentile>=90 and gradePercentile<100):
    print("You have an A")
    print(gradePercentile)
elif (gradePercentile>=80 and gradePercentile<=90):
    print("You have an B")
    print(gradePercentile)
elif (gradePercentile>=70 and gradePercentile<=80):
    print("You have an C")
    print(gradePercentile)
elif (gradePercentile>=60 and gradePercentile<=70):
    print("You have an D")
    print(gradePercentile)
elif (gradePercentile>=0 and gradePercentile<=60):
    print("You have an F")
    print(gradePercentile)
else:
    print("your either lying or messed up an input, this isn't possible!")
    print(gradePercentile)